/*
 * Copyright 2024 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"
#include "events_init.h"
#include "custom.h"


void setup_scr_Load_scrn_1(lv_ui *ui){

	//Write codes Load_scrn_1
	ui->Load_scrn_1 = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->Load_scrn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_load_scrn_1_main_main_default
	static lv_style_t style_load_scrn_1_main_main_default;
	if (style_load_scrn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_load_scrn_1_main_main_default);
	else
		lv_style_init(&style_load_scrn_1_main_main_default);
	lv_style_set_bg_color(&style_load_scrn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_load_scrn_1_main_main_default, 0);
	lv_obj_add_style(ui->Load_scrn_1, &style_load_scrn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Load_scrn_1_cont_1
	ui->Load_scrn_1_cont_1 = lv_obj_create(ui->Load_scrn_1);
	lv_obj_set_pos(ui->Load_scrn_1_cont_1, 0, 0);
	lv_obj_set_size(ui->Load_scrn_1_cont_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Load_scrn_1_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_load_scrn_1_cont_1_main_main_default
	static lv_style_t style_load_scrn_1_cont_1_main_main_default;
	if (style_load_scrn_1_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_load_scrn_1_cont_1_main_main_default);
	else
		lv_style_init(&style_load_scrn_1_cont_1_main_main_default);
	lv_style_set_radius(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_bg_color(&style_load_scrn_1_cont_1_main_main_default, lv_color_make(0x13, 0x01, 0x14));
	lv_style_set_bg_grad_color(&style_load_scrn_1_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_load_scrn_1_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_load_scrn_1_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_load_scrn_1_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_load_scrn_1_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_load_scrn_1_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_load_scrn_1_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_load_scrn_1_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_load_scrn_1_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->Load_scrn_1_cont_1, &style_load_scrn_1_cont_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Load_scrn_1_spinner_1
	ui->Load_scrn_1_spinner_1 = lv_spinner_create(ui->Load_scrn_1_cont_1, 10000, 104);
	lv_obj_set_pos(ui->Load_scrn_1_spinner_1, 560, 149);
	lv_obj_set_size(ui->Load_scrn_1_spinner_1, 195, 225);

	//Write style state: LV_STATE_DEFAULT for style_load_scrn_1_spinner_1_main_main_default
	static lv_style_t style_load_scrn_1_spinner_1_main_main_default;
	if (style_load_scrn_1_spinner_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_load_scrn_1_spinner_1_main_main_default);
	else
		lv_style_init(&style_load_scrn_1_spinner_1_main_main_default);
	lv_style_set_bg_color(&style_load_scrn_1_spinner_1_main_main_default, lv_color_make(0x13, 0x01, 0x14));
	lv_style_set_bg_grad_color(&style_load_scrn_1_spinner_1_main_main_default, lv_color_make(0xee, 0xee, 0xf6));
	lv_style_set_bg_grad_dir(&style_load_scrn_1_spinner_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_load_scrn_1_spinner_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_load_scrn_1_spinner_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_load_scrn_1_spinner_1_main_main_default, lv_color_make(0x2F, 0xDA, 0x64));
	lv_style_set_shadow_opa(&style_load_scrn_1_spinner_1_main_main_default, 213);
	lv_style_set_shadow_spread(&style_load_scrn_1_spinner_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_load_scrn_1_spinner_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_load_scrn_1_spinner_1_main_main_default, 0);
	lv_style_set_pad_left(&style_load_scrn_1_spinner_1_main_main_default, 5);
	lv_style_set_pad_right(&style_load_scrn_1_spinner_1_main_main_default, 5);
	lv_style_set_pad_top(&style_load_scrn_1_spinner_1_main_main_default, 5);
	lv_style_set_pad_bottom(&style_load_scrn_1_spinner_1_main_main_default, 5);
	lv_style_set_arc_color(&style_load_scrn_1_spinner_1_main_main_default, lv_color_make(0xf5, 0xf5, 0xf5));
	lv_style_set_arc_width(&style_load_scrn_1_spinner_1_main_main_default, 13);
	lv_obj_add_style(ui->Load_scrn_1_spinner_1, &style_load_scrn_1_spinner_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_load_scrn_1_spinner_1_main_indicator_default
	static lv_style_t style_load_scrn_1_spinner_1_main_indicator_default;
	if (style_load_scrn_1_spinner_1_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_load_scrn_1_spinner_1_main_indicator_default);
	else
		lv_style_init(&style_load_scrn_1_spinner_1_main_indicator_default);
	lv_style_set_arc_color(&style_load_scrn_1_spinner_1_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_arc_width(&style_load_scrn_1_spinner_1_main_indicator_default, 12);
	lv_obj_add_style(ui->Load_scrn_1_spinner_1, &style_load_scrn_1_spinner_1_main_indicator_default, LV_PART_INDICATOR|LV_STATE_DEFAULT);

	//Write codes Load_scrn_1_label_1
	ui->Load_scrn_1_label_1 = lv_label_create(ui->Load_scrn_1_cont_1);
	lv_obj_set_pos(ui->Load_scrn_1_label_1, 314, 375);
	lv_obj_set_size(ui->Load_scrn_1_label_1, 664, 234);
	lv_obj_set_scrollbar_mode(ui->Load_scrn_1_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->Load_scrn_1_label_1, "Please Follow The Bot.........\n\n\n\n\nBOT IS TRAVELLING TO NEXT ARTIFACT ");
	lv_label_set_long_mode(ui->Load_scrn_1_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_load_scrn_1_label_1_main_main_default
	static lv_style_t style_load_scrn_1_label_1_main_main_default;
	if (style_load_scrn_1_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_load_scrn_1_label_1_main_main_default);
	else
		lv_style_init(&style_load_scrn_1_label_1_main_main_default);
	lv_style_set_radius(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_load_scrn_1_label_1_main_main_default, lv_color_make(0x13, 0x01, 0x14));
	lv_style_set_bg_grad_color(&style_load_scrn_1_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_load_scrn_1_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_load_scrn_1_label_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_load_scrn_1_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_load_scrn_1_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_load_scrn_1_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_load_scrn_1_label_1_main_main_default, &lv_font_Alatsi_Regular_35);
	lv_style_set_text_letter_space(&style_load_scrn_1_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_load_scrn_1_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_load_scrn_1_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_load_scrn_1_label_1_main_main_default, 0);
	lv_obj_add_style(ui->Load_scrn_1_label_1, &style_load_scrn_1_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Init events for screen
	events_init_Load_scrn_1(ui);
}