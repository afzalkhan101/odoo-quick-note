/** @odoo-module **/

import { Component, onMounted, onWillUnmount, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";


export class GlobalQuickNote extends Component {
    static template = "quick_note.GlobalQuickNote";

    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");

        this.state = useState({
            isOpen: false,
            title: "",
            description: "",
            partner_id: false,
            category_id: false,
            priority: "0",
            note_date: new Date().toISOString().split("T")[0],
        });

        this.partners = [];
        this.categories = [];

        onMounted(() => {
            window.addEventListener(
                "keydown",
                this.onKeyDown.bind(this)
            );
        });

        onWillUnmount(() => {
            window.removeEventListener(
                "keydown",
                this.onKeyDown.bind(this)
            );
        });
    }

    async onKeyDown(event) {
        if (
            event.ctrlKey &&
            event.shiftKey &&
            event.key.toLowerCase() === "q"
        ) {
            event.preventDefault();
            event.stopPropagation();

            await this.openPopup();
        }

        if (event.key === "Escape" && this.state.isOpen) {
            this.closePopup();
        }
    }

    async openPopup() {
        await this.loadData();

        this.state.isOpen = true;
    }

    closePopup() {
        this.state.isOpen = false;
        this.resetForm();
    }

    async loadData() {
        this.partners = await this.orm.searchRead(
            "res.partner",
            [["active", "=", true]],
            ["name"],
            {
                limit: 100,
                order: "name",
            }
        );

        this.categories = await this.orm.searchRead(
            "quick.note.category",
            [["active", "=", true]],
            ["name"],
            {
                order: "name",
            }
        );
    }

    resetForm() {
        this.state.title = "";
        this.state.description = "";
        this.state.partner_id = false;
        this.state.category_id = false;
        this.state.priority = "0";
        this.state.note_date =
            new Date().toISOString().split("T")[0];
    }

    async saveNote() {
        if (!this.state.title.trim()) {
            this.notification.add(
                "Please enter a title.",
                {
                    type: "warning",
                }
            );

            return;
        }

        await this.orm.create(
            "quick.note",
            [{
                name: this.state.title,
                description: this.state.description,
                partner_id: this.state.partner_id || false,
                category_id: this.state.category_id || false,
                priority: this.state.priority,
                note_date: this.state.note_date,
            }]
        );

        this.notification.add(
            "Quick Note created successfully.",
            {
                type: "success",
            }
        );

        this.closePopup();
    }

    onTitleInput(event) {
        this.state.title = event.target.value;
    }

    onDescriptionInput(event) {
        this.state.description = event.target.value;
    }

    onPartnerChange(event) {
        this.state.partner_id =
            event.target.value
                ? Number(event.target.value)
                : false;
    }

    onCategoryChange(event) {
        this.state.category_id =
            event.target.value
                ? Number(event.target.value)
                : false;
    }

    onPriorityChange(event) {
        this.state.priority = event.target.value;
    }
}


registry
    .category("main_components")
    .add("quick_note.global_quick_note", {
        Component: GlobalQuickNote,
    });