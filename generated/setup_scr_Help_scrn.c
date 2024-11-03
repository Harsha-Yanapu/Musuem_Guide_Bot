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


void setup_scr_Help_scrn(lv_ui *ui){

	//Write codes Help_scrn
	ui->Help_scrn = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->Help_scrn, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_main_main_default
	static lv_style_t style_help_scrn_main_main_default;
	if (style_help_scrn_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_main_main_default);
	else
		lv_style_init(&style_help_scrn_main_main_default);
	lv_style_set_bg_color(&style_help_scrn_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_help_scrn_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn, &style_help_scrn_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_cont_1
	ui->Help_scrn_cont_1 = lv_obj_create(ui->Help_scrn);
	lv_obj_set_pos(ui->Help_scrn_cont_1, 0, 0);
	lv_obj_set_size(ui->Help_scrn_cont_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_cont_1_main_main_default
	static lv_style_t style_help_scrn_cont_1_main_main_default;
	if (style_help_scrn_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_cont_1_main_main_default);
	else
		lv_style_init(&style_help_scrn_cont_1_main_main_default);
	lv_style_set_radius(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_bg_color(&style_help_scrn_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_help_scrn_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_help_scrn_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_help_scrn_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_help_scrn_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_help_scrn_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_help_scrn_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_help_scrn_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_help_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_help_scrn_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn_cont_1, &style_help_scrn_cont_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_img_1
	ui->Help_scrn_img_1 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_1, 0, 0);
	lv_obj_set_size(ui->Help_scrn_img_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_1_main_main_default
	static lv_style_t style_help_scrn_img_1_main_main_default;
	if (style_help_scrn_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_1_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_1_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_1_main_main_default, lv_color_make(0xFF, 0x00, 0xB2));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_1_main_main_default, 48);
	lv_style_set_img_opa(&style_help_scrn_img_1_main_main_default, 177);
	lv_obj_add_style(ui->Help_scrn_img_1, &style_help_scrn_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_1,&_background_1280x720);
	lv_img_set_pivot(ui->Help_scrn_img_1, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_1, 0);

	//Write codes Help_scrn_label_1
	ui->Help_scrn_label_1 = lv_label_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_label_1, 315, 8);
	lv_obj_set_size(ui->Help_scrn_label_1, 357, 704);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->Help_scrn_label_1, "Sign commands:\n\nNEXT   -------->\n\n\nSTART  ------->\n\n\nBACK   -------->\n\n\nONE   ---------->\n\n\nTWO   --------->\n\n\nTHREE   ------->\n\n\nFOUR   ------->\n\n\nFIVE   -------->\n");
	lv_label_set_long_mode(ui->Help_scrn_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_label_1_main_main_default
	static lv_style_t style_help_scrn_label_1_main_main_default;
	if (style_help_scrn_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_label_1_main_main_default);
	else
		lv_style_init(&style_help_scrn_label_1_main_main_default);
	lv_style_set_radius(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_help_scrn_label_1_main_main_default, lv_color_make(0xC3, 0x4B, 0xB5));
	lv_style_set_bg_grad_color(&style_help_scrn_label_1_main_main_default, lv_color_make(0x00, 0x01, 0x01));
	lv_style_set_bg_grad_dir(&style_help_scrn_label_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_help_scrn_label_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_help_scrn_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_help_scrn_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_help_scrn_label_1_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_letter_space(&style_help_scrn_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_help_scrn_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_help_scrn_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_help_scrn_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_help_scrn_label_1_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn_label_1, &style_help_scrn_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_label_2
	ui->Help_scrn_label_2 = lv_label_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_label_2, 717, 7);
	lv_obj_set_size(ui->Help_scrn_label_2, 506, 123);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_label_2, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->Help_scrn_label_2, "Say the Wake Word \"HEY NXP\" , To Start the Voice Recognition");
	lv_label_set_long_mode(ui->Help_scrn_label_2, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_label_2_main_main_default
	static lv_style_t style_help_scrn_label_2_main_main_default;
	if (style_help_scrn_label_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_label_2_main_main_default);
	else
		lv_style_init(&style_help_scrn_label_2_main_main_default);
	lv_style_set_radius(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_bg_color(&style_help_scrn_label_2_main_main_default, lv_color_make(0xc3, 0x4b, 0xb5));
	lv_style_set_bg_grad_color(&style_help_scrn_label_2_main_main_default, lv_color_make(0x06, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_help_scrn_label_2_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_help_scrn_label_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_shadow_color(&style_help_scrn_label_2_main_main_default, lv_color_make(0x00, 0x01, 0x01));
	lv_style_set_shadow_opa(&style_help_scrn_label_2_main_main_default, 238);
	lv_style_set_shadow_spread(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_text_color(&style_help_scrn_label_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_help_scrn_label_2_main_main_default, &lv_font_Acme_Regular_34);
	lv_style_set_text_letter_space(&style_help_scrn_label_2_main_main_default, 3);
	lv_style_set_text_line_space(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_text_align(&style_help_scrn_label_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_pad_right(&style_help_scrn_label_2_main_main_default, 0);
	lv_style_set_pad_top(&style_help_scrn_label_2_main_main_default, 9);
	lv_style_set_pad_bottom(&style_help_scrn_label_2_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn_label_2, &style_help_scrn_label_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_label_3
	ui->Help_scrn_label_3 = lv_label_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_label_3, 835, 139);
	lv_obj_set_size(ui->Help_scrn_label_3, 321, 574);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_label_3, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->Help_scrn_label_3, "Voice Commands:\n\nNEXT\n\nSTART\n\nBACK\n\nHISTORY\n\nDESCRIPTION\n\nDEPICTION\n\nINTERPRETATION\n\nSTYLE\n\n");
	lv_label_set_long_mode(ui->Help_scrn_label_3, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_label_3_main_main_default
	static lv_style_t style_help_scrn_label_3_main_main_default;
	if (style_help_scrn_label_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_label_3_main_main_default);
	else
		lv_style_init(&style_help_scrn_label_3_main_main_default);
	lv_style_set_radius(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_bg_color(&style_help_scrn_label_3_main_main_default, lv_color_make(0xC3, 0x4B, 0xB5));
	lv_style_set_bg_grad_color(&style_help_scrn_label_3_main_main_default, lv_color_make(0x04, 0x0d, 0x16));
	lv_style_set_bg_grad_dir(&style_help_scrn_label_3_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_help_scrn_label_3_main_main_default, 255);
	lv_style_set_shadow_width(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_shadow_color(&style_help_scrn_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_label_3_main_main_default, 255);
	lv_style_set_shadow_spread(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_text_color(&style_help_scrn_label_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_help_scrn_label_3_main_main_default, &lv_font_Acme_Regular_32);
	lv_style_set_text_letter_space(&style_help_scrn_label_3_main_main_default, 2);
	lv_style_set_text_line_space(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_text_align(&style_help_scrn_label_3_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_pad_right(&style_help_scrn_label_3_main_main_default, 0);
	lv_style_set_pad_top(&style_help_scrn_label_3_main_main_default, 8);
	lv_style_set_pad_bottom(&style_help_scrn_label_3_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn_label_3, &style_help_scrn_label_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_img_3
	ui->Help_scrn_img_3 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_3, 585, 55);
	lv_obj_set_size(ui->Help_scrn_img_3, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_3_main_main_default
	static lv_style_t style_help_scrn_img_3_main_main_default;
	if (style_help_scrn_img_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_3_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_3_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_3_main_main_default, lv_color_make(0xfd, 0xfd, 0xfd));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_3_main_main_default, 255);
	lv_style_set_img_opa(&style_help_scrn_img_3_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_3, &style_help_scrn_img_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_3, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_3,&_Next_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_3, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_3, 0);

	//Write codes Help_scrn_img_4
	ui->Help_scrn_img_4 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_4, 577, 136);
	lv_obj_set_size(ui->Help_scrn_img_4, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_4, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_4_main_main_default
	static lv_style_t style_help_scrn_img_4_main_main_default;
	if (style_help_scrn_img_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_4_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_4_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_4_main_main_default, 225);
	lv_style_set_img_opa(&style_help_scrn_img_4_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_4, &style_help_scrn_img_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_4, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_4,&_Ok_Enter_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_4, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_4, 0);

	//Write codes Help_scrn_img_5
	ui->Help_scrn_img_5 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_5, 580, 226);
	lv_obj_set_size(ui->Help_scrn_img_5, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_5, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_5_main_main_default
	static lv_style_t style_help_scrn_img_5_main_main_default;
	if (style_help_scrn_img_5_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_5_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_5_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_5_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_5_main_main_default, 223);
	lv_style_set_img_opa(&style_help_scrn_img_5_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_5, &style_help_scrn_img_5_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_5, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_5,&_Backthumb_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_5, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_5, 0);

	//Write codes Help_scrn_img_6
	ui->Help_scrn_img_6 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_6, 575, 310);
	lv_obj_set_size(ui->Help_scrn_img_6, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_6, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_6_main_main_default
	static lv_style_t style_help_scrn_img_6_main_main_default;
	if (style_help_scrn_img_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_6_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_6_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_6_main_main_default, 247);
	lv_style_set_img_opa(&style_help_scrn_img_6_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_6, &style_help_scrn_img_6_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_6, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_6,&_One_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_6, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_6, 0);

	//Write codes Help_scrn_img_7
	ui->Help_scrn_img_7 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_7, 578, 397);
	lv_obj_set_size(ui->Help_scrn_img_7, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_7, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_7_main_main_default
	static lv_style_t style_help_scrn_img_7_main_main_default;
	if (style_help_scrn_img_7_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_7_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_7_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_7_main_main_default, lv_color_make(0xfe, 0xfe, 0xfe));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_7_main_main_default, 234);
	lv_style_set_img_opa(&style_help_scrn_img_7_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_7, &style_help_scrn_img_7_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_7, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_7,&_Two_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_7, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_7, 0);

	//Write codes Help_scrn_img_8
	ui->Help_scrn_img_8 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_8, 578, 474);
	lv_obj_set_size(ui->Help_scrn_img_8, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_8, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_8_main_main_default
	static lv_style_t style_help_scrn_img_8_main_main_default;
	if (style_help_scrn_img_8_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_8_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_8_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_8_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_8_main_main_default, 255);
	lv_style_set_img_opa(&style_help_scrn_img_8_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_8, &style_help_scrn_img_8_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_8, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_8,&_Three_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_8, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_8, 0);

	//Write codes Help_scrn_img_9
	ui->Help_scrn_img_9 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_9, 577, 556);
	lv_obj_set_size(ui->Help_scrn_img_9, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_9, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_9_main_main_default
	static lv_style_t style_help_scrn_img_9_main_main_default;
	if (style_help_scrn_img_9_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_9_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_9_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_9_main_main_default, lv_color_make(0xf3, 0xf3, 0xf3));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_9_main_main_default, 239);
	lv_style_set_img_opa(&style_help_scrn_img_9_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_9, &style_help_scrn_img_9_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_9, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_9,&_Four_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_9, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_9, 0);

	//Write codes Help_scrn_img_10
	ui->Help_scrn_img_10 = lv_img_create(ui->Help_scrn_cont_1);
	lv_obj_set_pos(ui->Help_scrn_img_10, 574, 636);
	lv_obj_set_size(ui->Help_scrn_img_10, 83, 61);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_10, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_10_main_main_default
	static lv_style_t style_help_scrn_img_10_main_main_default;
	if (style_help_scrn_img_10_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_10_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_10_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_10_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_10_main_main_default, 255);
	lv_style_set_img_opa(&style_help_scrn_img_10_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_10, &style_help_scrn_img_10_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_10, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_10,&_Five_83x61);
	lv_img_set_pivot(ui->Help_scrn_img_10, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_10, 0);

	//Write codes Help_scrn_cont_2
	ui->Help_scrn_cont_2 = lv_obj_create(ui->Help_scrn);
	lv_obj_set_pos(ui->Help_scrn_cont_2, 18, 14);
	lv_obj_set_size(ui->Help_scrn_cont_2, 266, 109);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_cont_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_cont_2_main_main_default
	static lv_style_t style_help_scrn_cont_2_main_main_default;
	if (style_help_scrn_cont_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_cont_2_main_main_default);
	else
		lv_style_init(&style_help_scrn_cont_2_main_main_default);
	lv_style_set_radius(&style_help_scrn_cont_2_main_main_default, 9);
	lv_style_set_bg_color(&style_help_scrn_cont_2_main_main_default, lv_color_make(0x41, 0x60, 0x6E));
	lv_style_set_bg_grad_color(&style_help_scrn_cont_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_help_scrn_cont_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_help_scrn_cont_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_help_scrn_cont_2_main_main_default, 1);
	lv_style_set_shadow_color(&style_help_scrn_cont_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_help_scrn_cont_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_help_scrn_cont_2_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_cont_2_main_main_default, 3);
	lv_style_set_shadow_ofs_y(&style_help_scrn_cont_2_main_main_default, 6);
	lv_style_set_border_color(&style_help_scrn_cont_2_main_main_default, lv_color_make(0x00, 0x04, 0x06));
	lv_style_set_border_width(&style_help_scrn_cont_2_main_main_default, 6);
	lv_style_set_border_opa(&style_help_scrn_cont_2_main_main_default, 255);
	lv_style_set_pad_left(&style_help_scrn_cont_2_main_main_default, 0);
	lv_style_set_pad_right(&style_help_scrn_cont_2_main_main_default, 0);
	lv_style_set_pad_top(&style_help_scrn_cont_2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_help_scrn_cont_2_main_main_default, 0);
	lv_obj_add_style(ui->Help_scrn_cont_2, &style_help_scrn_cont_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Help_scrn_img_2
	ui->Help_scrn_img_2 = lv_img_create(ui->Help_scrn_cont_2);
	lv_obj_set_pos(ui->Help_scrn_img_2, 139, 4);
	lv_obj_set_size(ui->Help_scrn_img_2, 100, 89);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_img_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_img_2_main_main_default
	static lv_style_t style_help_scrn_img_2_main_main_default;
	if (style_help_scrn_img_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_img_2_main_main_default);
	else
		lv_style_init(&style_help_scrn_img_2_main_main_default);
	lv_style_set_img_recolor(&style_help_scrn_img_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_help_scrn_img_2_main_main_default, 233);
	lv_style_set_img_opa(&style_help_scrn_img_2_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_img_2, &style_help_scrn_img_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Help_scrn_img_2, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Help_scrn_img_2,&_Backthumb_100x89);
	lv_img_set_pivot(ui->Help_scrn_img_2, 50,50);
	lv_img_set_angle(ui->Help_scrn_img_2, 0);

	//Write codes Help_scrn_imgbtn_1
	ui->Help_scrn_imgbtn_1 = lv_imgbtn_create(ui->Help_scrn_cont_2);
	lv_obj_set_pos(ui->Help_scrn_imgbtn_1, 8, -1);
	lv_obj_set_size(ui->Help_scrn_imgbtn_1, 112, 103);
	lv_obj_set_scrollbar_mode(ui->Help_scrn_imgbtn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_help_scrn_imgbtn_1_main_main_default
	static lv_style_t style_help_scrn_imgbtn_1_main_main_default;
	if (style_help_scrn_imgbtn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_imgbtn_1_main_main_default);
	else
		lv_style_init(&style_help_scrn_imgbtn_1_main_main_default);
	lv_style_set_shadow_width(&style_help_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_help_scrn_imgbtn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_imgbtn_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_help_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_text_color(&style_help_scrn_imgbtn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_help_scrn_imgbtn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_help_scrn_imgbtn_1_main_main_default, lv_color_make(0x71, 0x17, 0x73));
	lv_style_set_img_recolor_opa(&style_help_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_img_opa(&style_help_scrn_imgbtn_1_main_main_default, 255);
	lv_obj_add_style(ui->Help_scrn_imgbtn_1, &style_help_scrn_imgbtn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_help_scrn_imgbtn_1_main_main_pressed
	static lv_style_t style_help_scrn_imgbtn_1_main_main_pressed;
	if (style_help_scrn_imgbtn_1_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_imgbtn_1_main_main_pressed);
	else
		lv_style_init(&style_help_scrn_imgbtn_1_main_main_pressed);
	lv_style_set_shadow_width(&style_help_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_color(&style_help_scrn_imgbtn_1_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_imgbtn_1_main_main_pressed, 255);
	lv_style_set_shadow_spread(&style_help_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_text_color(&style_help_scrn_imgbtn_1_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_img_recolor(&style_help_scrn_imgbtn_1_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_help_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_img_opa(&style_help_scrn_imgbtn_1_main_main_pressed, 255);
	lv_obj_add_style(ui->Help_scrn_imgbtn_1, &style_help_scrn_imgbtn_1_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_help_scrn_imgbtn_1_main_main_checked
	static lv_style_t style_help_scrn_imgbtn_1_main_main_checked;
	if (style_help_scrn_imgbtn_1_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_help_scrn_imgbtn_1_main_main_checked);
	else
		lv_style_init(&style_help_scrn_imgbtn_1_main_main_checked);
	lv_style_set_shadow_width(&style_help_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_color(&style_help_scrn_imgbtn_1_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_help_scrn_imgbtn_1_main_main_checked, 255);
	lv_style_set_shadow_spread(&style_help_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_ofs_x(&style_help_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_ofs_y(&style_help_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_text_color(&style_help_scrn_imgbtn_1_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_img_recolor(&style_help_scrn_imgbtn_1_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_help_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_img_opa(&style_help_scrn_imgbtn_1_main_main_checked, 255);
	lv_obj_add_style(ui->Help_scrn_imgbtn_1, &style_help_scrn_imgbtn_1_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->Help_scrn_imgbtn_1, LV_IMGBTN_STATE_RELEASED, NULL, &_Backbutton_alpha_112x103, NULL);
	lv_imgbtn_set_src(ui->Help_scrn_imgbtn_1, LV_IMGBTN_STATE_PRESSED, NULL, &_Backbutton_alpha_112x103, NULL);
	lv_obj_add_flag(ui->Help_scrn_imgbtn_1, LV_OBJ_FLAG_CHECKABLE);

	//Init events for screen
	events_init_Help_scrn(ui);
}