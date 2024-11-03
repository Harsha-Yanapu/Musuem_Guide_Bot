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


void setup_scr_Art_05(lv_ui *ui){

	//Write codes Art_05
	ui->Art_05 = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->Art_05, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_main_main_default
	static lv_style_t style_art_05_main_main_default;
	if (style_art_05_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_main_main_default);
	else
		lv_style_init(&style_art_05_main_main_default);
	lv_style_set_bg_color(&style_art_05_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_art_05_main_main_default, 0);
	lv_obj_add_style(ui->Art_05, &style_art_05_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_05_cont_1
	ui->Art_05_cont_1 = lv_obj_create(ui->Art_05);
	lv_obj_set_pos(ui->Art_05_cont_1, -1, 0);
	lv_obj_set_size(ui->Art_05_cont_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Art_05_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_cont_1_main_main_default
	static lv_style_t style_art_05_cont_1_main_main_default;
	if (style_art_05_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_cont_1_main_main_default);
	else
		lv_style_init(&style_art_05_cont_1_main_main_default);
	lv_style_set_radius(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_bg_color(&style_art_05_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_art_05_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_art_05_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_art_05_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_art_05_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_art_05_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_art_05_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_art_05_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_art_05_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_art_05_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_art_05_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->Art_05_cont_1, &style_art_05_cont_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_05_img_1
	ui->Art_05_img_1 = lv_img_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_img_1, 0, 0);
	lv_obj_set_size(ui->Art_05_img_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Art_05_img_1, LV_SCROLLBAR_MODE_ON);

	//Write style state: LV_STATE_DEFAULT for style_art_05_img_1_main_main_default
	static lv_style_t style_art_05_img_1_main_main_default;
	if (style_art_05_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_img_1_main_main_default);
	else
		lv_style_init(&style_art_05_img_1_main_main_default);
	lv_style_set_img_recolor(&style_art_05_img_1_main_main_default, lv_color_make(0xFF, 0x00, 0xB2));
	lv_style_set_img_recolor_opa(&style_art_05_img_1_main_main_default, 53);
	lv_style_set_img_opa(&style_art_05_img_1_main_main_default, 186);
	lv_obj_add_style(ui->Art_05_img_1, &style_art_05_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_05_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_05_img_1,&_background_1280x720);
	lv_img_set_pivot(ui->Art_05_img_1, 50,50);
	lv_img_set_angle(ui->Art_05_img_1, 0);

	//Write codes Art_05_img_2
	ui->Art_05_img_2 = lv_img_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_img_2, 85, 38);
	lv_obj_set_size(ui->Art_05_img_2, 287, 371);
	lv_obj_set_scrollbar_mode(ui->Art_05_img_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_img_2_main_main_default
	static lv_style_t style_art_05_img_2_main_main_default;
	if (style_art_05_img_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_img_2_main_main_default);
	else
		lv_style_init(&style_art_05_img_2_main_main_default);
	lv_style_set_img_recolor(&style_art_05_img_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_05_img_2_main_main_default, 0);
	lv_style_set_img_opa(&style_art_05_img_2_main_main_default, 255);
	lv_obj_add_style(ui->Art_05_img_2, &style_art_05_img_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_05_img_2, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_05_img_2,&_Art_05_287x371);
	lv_img_set_pivot(ui->Art_05_img_2, 50,50);
	lv_img_set_angle(ui->Art_05_img_2, 0);

	//Write codes Art_05_label_1
	ui->Art_05_label_1 = lv_label_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_label_1, 509, 71);
	lv_obj_set_size(ui->Art_05_label_1, 754, 306);
	lv_obj_set_scrollbar_mode(ui->Art_05_label_1, LV_SCROLLBAR_MODE_ON);
	lv_label_set_text(ui->Art_05_label_1, "A yogini is a female master practitioner of tantra and yoga, as well as a formal term of respect for female Hindu or Buddhist spiritual teachers in the Indian subcontinent, Southeast Asia and Greater Tibet. The term is the feminine Sanskrit word of the masculine yogi, while the term \"yogin\"  is used in neutral, masculine or feminine sense.\n\nA yogini, in some contexts, is the sacred feminine force made incarnate, as an aspect of Mahadevi, and revered in the yogini temples of India. These often revere a group of 64 yoginis, and are named as such, but can also have 42 or 81 yoginis. The names of the 64 yoginis vary in different classifications.");
	lv_label_set_long_mode(ui->Art_05_label_1, LV_LABEL_LONG_SCROLL);

	//Write style state: LV_STATE_DEFAULT for style_art_05_label_1_main_main_default
	static lv_style_t style_art_05_label_1_main_main_default;
	if (style_art_05_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_label_1_main_main_default);
	else
		lv_style_init(&style_art_05_label_1_main_main_default);
	lv_style_set_radius(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_art_05_label_1_main_main_default, lv_color_make(0x76, 0x2d, 0x6d));
	lv_style_set_bg_grad_color(&style_art_05_label_1_main_main_default, lv_color_make(0x0d, 0x01, 0x0c));
	lv_style_set_bg_grad_dir(&style_art_05_label_1_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_art_05_label_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_art_05_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_art_05_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_art_05_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_05_label_1_main_main_default, &lv_font_Abel_regular_25);
	lv_style_set_text_letter_space(&style_art_05_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_art_05_label_1_main_main_default, 5);
	lv_style_set_text_align(&style_art_05_label_1_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_art_05_label_1_main_main_default, 7);
	lv_style_set_pad_right(&style_art_05_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_art_05_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_art_05_label_1_main_main_default, 0);
	lv_obj_add_style(ui->Art_05_label_1, &style_art_05_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_05_ta_1
	ui->Art_05_ta_1 = lv_textarea_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_ta_1, 640, 15);
	lv_obj_set_size(ui->Art_05_ta_1, 411, 41);
	lv_obj_set_scrollbar_mode(ui->Art_05_ta_1, LV_SCROLLBAR_MODE_ON);

	//Write style state: LV_STATE_DEFAULT for style_art_05_ta_1_main_main_default
	static lv_style_t style_art_05_ta_1_main_main_default;
	if (style_art_05_ta_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_ta_1_main_main_default);
	else
		lv_style_init(&style_art_05_ta_1_main_main_default);
	lv_style_set_radius(&style_art_05_ta_1_main_main_default, 5);
	lv_style_set_bg_color(&style_art_05_ta_1_main_main_default, lv_color_make(0xb8, 0x82, 0xab));
	lv_style_set_bg_grad_color(&style_art_05_ta_1_main_main_default, lv_color_make(0x6b, 0x37, 0x86));
	lv_style_set_bg_grad_dir(&style_art_05_ta_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_05_ta_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_ta_1_main_main_default, 2);
	lv_style_set_shadow_color(&style_art_05_ta_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_05_ta_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_ta_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_05_ta_1_main_main_default, -5);
	lv_style_set_shadow_ofs_y(&style_art_05_ta_1_main_main_default, -3);
	lv_style_set_border_color(&style_art_05_ta_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_05_ta_1_main_main_default, 3);
	lv_style_set_border_opa(&style_art_05_ta_1_main_main_default, 255);
	lv_style_set_text_color(&style_art_05_ta_1_main_main_default, lv_color_make(0xfe, 0xfe, 0xfe));
	lv_style_set_text_font(&style_art_05_ta_1_main_main_default, &lv_font_Acme_Regular_29);
	lv_style_set_text_letter_space(&style_art_05_ta_1_main_main_default, 2);
	lv_style_set_text_align(&style_art_05_ta_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_art_05_ta_1_main_main_default, 4);
	lv_style_set_pad_right(&style_art_05_ta_1_main_main_default, 4);
	lv_style_set_pad_top(&style_art_05_ta_1_main_main_default, 4);
	lv_style_set_pad_bottom(&style_art_05_ta_1_main_main_default, 4);
	lv_obj_add_style(ui->Art_05_ta_1, &style_art_05_ta_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_art_05_ta_1_main_scrollbar_default
	static lv_style_t style_art_05_ta_1_main_scrollbar_default;
	if (style_art_05_ta_1_main_scrollbar_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_ta_1_main_scrollbar_default);
	else
		lv_style_init(&style_art_05_ta_1_main_scrollbar_default);
	lv_style_set_radius(&style_art_05_ta_1_main_scrollbar_default, 0);
	lv_style_set_bg_color(&style_art_05_ta_1_main_scrollbar_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_opa(&style_art_05_ta_1_main_scrollbar_default, 255);
	lv_obj_add_style(ui->Art_05_ta_1, &style_art_05_ta_1_main_scrollbar_default, LV_PART_SCROLLBAR|LV_STATE_DEFAULT);
	lv_textarea_set_text(ui->Art_05_ta_1,"ARTIFACT-05    :     YOGINI");

	//Write codes Art_05_btn_1
	ui->Art_05_btn_1 = lv_btn_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_btn_1, 514, 430);
	lv_obj_set_size(ui->Art_05_btn_1, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_05_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_btn_1_main_main_default
	static lv_style_t style_art_05_btn_1_main_main_default;
	if (style_art_05_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_btn_1_main_main_default);
	else
		lv_style_init(&style_art_05_btn_1_main_main_default);
	lv_style_set_radius(&style_art_05_btn_1_main_main_default, 9);
	lv_style_set_bg_color(&style_art_05_btn_1_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_05_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_05_btn_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_05_btn_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_btn_1_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_05_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_05_btn_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_btn_1_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_05_btn_1_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_05_btn_1_main_main_default, 4);
	lv_style_set_border_color(&style_art_05_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_05_btn_1_main_main_default, 5);
	lv_style_set_border_opa(&style_art_05_btn_1_main_main_default, 255);
	lv_style_set_text_color(&style_art_05_btn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_05_btn_1_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_05_btn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_05_btn_1, &style_art_05_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_05_btn_1_label = lv_label_create(ui->Art_05_btn_1);
	lv_label_set_text(ui->Art_05_btn_1_label, "1. HISTORY");
	lv_obj_set_style_pad_all(ui->Art_05_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_05_btn_1_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_05_img_3
	ui->Art_05_img_3 = lv_img_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_img_3, 519, 436);
	lv_obj_set_size(ui->Art_05_img_3, 62, 60);
	lv_obj_set_scrollbar_mode(ui->Art_05_img_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_img_3_main_main_default
	static lv_style_t style_art_05_img_3_main_main_default;
	if (style_art_05_img_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_img_3_main_main_default);
	else
		lv_style_init(&style_art_05_img_3_main_main_default);
	lv_style_set_img_recolor(&style_art_05_img_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_05_img_3_main_main_default, 255);
	lv_style_set_img_opa(&style_art_05_img_3_main_main_default, 255);
	lv_obj_add_style(ui->Art_05_img_3, &style_art_05_img_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_05_img_3, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_05_img_3,&_One_62x60);
	lv_img_set_pivot(ui->Art_05_img_3, 50,50);
	lv_img_set_angle(ui->Art_05_img_3, 0);

	//Write codes Art_05_btn_2
	ui->Art_05_btn_2 = lv_btn_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_btn_2, 925, 435);
	lv_obj_set_size(ui->Art_05_btn_2, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_05_btn_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_btn_2_main_main_default
	static lv_style_t style_art_05_btn_2_main_main_default;
	if (style_art_05_btn_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_btn_2_main_main_default);
	else
		lv_style_init(&style_art_05_btn_2_main_main_default);
	lv_style_set_radius(&style_art_05_btn_2_main_main_default, 9);
	lv_style_set_bg_color(&style_art_05_btn_2_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_05_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_05_btn_2_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_05_btn_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_btn_2_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_05_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_05_btn_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_btn_2_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_05_btn_2_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_05_btn_2_main_main_default, 4);
	lv_style_set_border_color(&style_art_05_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_05_btn_2_main_main_default, 5);
	lv_style_set_border_opa(&style_art_05_btn_2_main_main_default, 255);
	lv_style_set_text_color(&style_art_05_btn_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_05_btn_2_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_05_btn_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_05_btn_2, &style_art_05_btn_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_05_btn_2_label = lv_label_create(ui->Art_05_btn_2);
	lv_label_set_text(ui->Art_05_btn_2_label, "2. DESCRIPTION");
	lv_obj_set_style_pad_all(ui->Art_05_btn_2, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_05_btn_2_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_05_img_4
	ui->Art_05_img_4 = lv_img_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_img_4, 929, 438);
	lv_obj_set_size(ui->Art_05_img_4, 70, 61);
	lv_obj_set_scrollbar_mode(ui->Art_05_img_4, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_img_4_main_main_default
	static lv_style_t style_art_05_img_4_main_main_default;
	if (style_art_05_img_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_img_4_main_main_default);
	else
		lv_style_init(&style_art_05_img_4_main_main_default);
	lv_style_set_img_recolor(&style_art_05_img_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_05_img_4_main_main_default, 252);
	lv_style_set_img_opa(&style_art_05_img_4_main_main_default, 255);
	lv_obj_add_style(ui->Art_05_img_4, &style_art_05_img_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_05_img_4, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_05_img_4,&_Two_70x61);
	lv_img_set_pivot(ui->Art_05_img_4, 50,50);
	lv_img_set_angle(ui->Art_05_img_4, 0);

	//Write codes Art_05_btn_4
	ui->Art_05_btn_4 = lv_btn_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_btn_4, 515, 551);
	lv_obj_set_size(ui->Art_05_btn_4, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_05_btn_4, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_btn_4_main_main_default
	static lv_style_t style_art_05_btn_4_main_main_default;
	if (style_art_05_btn_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_btn_4_main_main_default);
	else
		lv_style_init(&style_art_05_btn_4_main_main_default);
	lv_style_set_radius(&style_art_05_btn_4_main_main_default, 9);
	lv_style_set_bg_color(&style_art_05_btn_4_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_05_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_05_btn_4_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_05_btn_4_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_05_btn_4_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_05_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_05_btn_4_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_05_btn_4_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_05_btn_4_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_05_btn_4_main_main_default, 4);
	lv_style_set_border_color(&style_art_05_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_05_btn_4_main_main_default, 5);
	lv_style_set_border_opa(&style_art_05_btn_4_main_main_default, 255);
	lv_style_set_text_color(&style_art_05_btn_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_05_btn_4_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_05_btn_4_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_05_btn_4, &style_art_05_btn_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_05_btn_4_label = lv_label_create(ui->Art_05_btn_4);
	lv_label_set_text(ui->Art_05_btn_4_label, "    NEXT ART");
	lv_obj_set_style_pad_all(ui->Art_05_btn_4, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_05_btn_4_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_05_img_6
	ui->Art_05_img_6 = lv_img_create(ui->Art_05_cont_1);
	lv_obj_set_pos(ui->Art_05_img_6, 533, 553);
	lv_obj_set_size(ui->Art_05_img_6, 69, 70);
	lv_obj_set_scrollbar_mode(ui->Art_05_img_6, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_05_img_6_main_main_default
	static lv_style_t style_art_05_img_6_main_main_default;
	if (style_art_05_img_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_05_img_6_main_main_default);
	else
		lv_style_init(&style_art_05_img_6_main_main_default);
	lv_style_set_img_recolor(&style_art_05_img_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_05_img_6_main_main_default, 251);
	lv_style_set_img_opa(&style_art_05_img_6_main_main_default, 255);
	lv_obj_add_style(ui->Art_05_img_6, &style_art_05_img_6_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_05_img_6, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_05_img_6,&_Next_69x70);
	lv_img_set_pivot(ui->Art_05_img_6, 50,50);
	lv_img_set_angle(ui->Art_05_img_6, 0);

	//Write codes Art_05_video_1
	ui->Art_05_video_1 = lv_video_create(ui->Art_05_cont_1, 422, 263);
	lv_video_set_status(ui->Art_05_video_1, 0);
#if LV_USE_GUIDER_SIMULATOR
	lv_video_set_src(ui->Art_05_video_1,"");
#else
#endif
	lv_obj_set_pos(ui->Art_05_video_1, 28, 433);
	lv_obj_set_size(ui->Art_05_video_1, 422, 263);

	//Init events for screen
	events_init_Art_05(ui);
}