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


void setup_scr_Art_03_hist(lv_ui *ui){

	//Write codes Art_03_hist
	ui->Art_03_hist = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_main_main_default
	static lv_style_t style_art_03_hist_main_main_default;
	if (style_art_03_hist_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_main_main_default);
	else
		lv_style_init(&style_art_03_hist_main_main_default);
	lv_style_set_bg_color(&style_art_03_hist_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_art_03_hist_main_main_default, 0);
	lv_obj_add_style(ui->Art_03_hist, &style_art_03_hist_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_03_hist_cont_1
	ui->Art_03_hist_cont_1 = lv_obj_create(ui->Art_03_hist);
	lv_obj_set_pos(ui->Art_03_hist_cont_1, -1, 0);
	lv_obj_set_size(ui->Art_03_hist_cont_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_cont_1_main_main_default
	static lv_style_t style_art_03_hist_cont_1_main_main_default;
	if (style_art_03_hist_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_cont_1_main_main_default);
	else
		lv_style_init(&style_art_03_hist_cont_1_main_main_default);
	lv_style_set_radius(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_bg_color(&style_art_03_hist_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_art_03_hist_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_art_03_hist_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_art_03_hist_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_art_03_hist_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_art_03_hist_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_art_03_hist_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_art_03_hist_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_art_03_hist_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_art_03_hist_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->Art_03_hist_cont_1, &style_art_03_hist_cont_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_03_hist_img_1
	ui->Art_03_hist_img_1 = lv_img_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_img_1, 0, 0);
	lv_obj_set_size(ui->Art_03_hist_img_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_img_1, LV_SCROLLBAR_MODE_ON);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_img_1_main_main_default
	static lv_style_t style_art_03_hist_img_1_main_main_default;
	if (style_art_03_hist_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_img_1_main_main_default);
	else
		lv_style_init(&style_art_03_hist_img_1_main_main_default);
	lv_style_set_img_recolor(&style_art_03_hist_img_1_main_main_default, lv_color_make(0xFF, 0x00, 0xB2));
	lv_style_set_img_recolor_opa(&style_art_03_hist_img_1_main_main_default, 53);
	lv_style_set_img_opa(&style_art_03_hist_img_1_main_main_default, 186);
	lv_obj_add_style(ui->Art_03_hist_img_1, &style_art_03_hist_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_03_hist_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_03_hist_img_1,&_background_1280x720);
	lv_img_set_pivot(ui->Art_03_hist_img_1, 50,50);
	lv_img_set_angle(ui->Art_03_hist_img_1, 0);

	//Write codes Art_03_hist_label_1
	ui->Art_03_hist_label_1 = lv_label_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_label_1, 507, 70);
	lv_obj_set_size(ui->Art_03_hist_label_1, 758, 306);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_label_1, LV_SCROLLBAR_MODE_ON);
	lv_label_set_text(ui->Art_03_hist_label_1, "The Didarganj Yakshi was excavated on the banks of the Ganges River, at the hamlet of Didarganj Kadam Rasual, northeast of the Qadam-i-Rasul Mosque in Patna City, on 18 October 1917 by the villagers and by the noted archaeologist and historian, Professor J N Samaddar Professor Samaddar, with the help of the then president of Patna Museum Committee and member of Board of Revenue, Mr. E. H. C. Walsh and Dr. D. B. Spooner, the noted archaeologist, retrieved the figure in Patna Museum, Patna.\n\nThe statue's nose was damaged during a travelling exhibition, The Festival of India, en route to Smithsonian Institution and the National Gallery of Art, Washington, D.C., leading to a decision not to send it abroad again.\n\nTo celebrate the centenary year of the excavation, Sunita Bharti, a theatre director from Patna, produced and directed a play, Yakshini, in 2017. It was staged by the Indian Council for Cultural Relations (ICCR, Govt. of India) and the Indira Gandhi National Centre for the Arts (IGNCA, Govt. of India), New Delhi.");
	lv_label_set_long_mode(ui->Art_03_hist_label_1, LV_LABEL_LONG_SCROLL);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_label_1_main_main_default
	static lv_style_t style_art_03_hist_label_1_main_main_default;
	if (style_art_03_hist_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_label_1_main_main_default);
	else
		lv_style_init(&style_art_03_hist_label_1_main_main_default);
	lv_style_set_radius(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_art_03_hist_label_1_main_main_default, lv_color_make(0x76, 0x2d, 0x6d));
	lv_style_set_bg_grad_color(&style_art_03_hist_label_1_main_main_default, lv_color_make(0x0d, 0x01, 0x0c));
	lv_style_set_bg_grad_dir(&style_art_03_hist_label_1_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_art_03_hist_label_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_art_03_hist_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_art_03_hist_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_art_03_hist_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_03_hist_label_1_main_main_default, &lv_font_Abel_regular_25);
	lv_style_set_text_letter_space(&style_art_03_hist_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_art_03_hist_label_1_main_main_default, 5);
	lv_style_set_text_align(&style_art_03_hist_label_1_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_style_set_pad_left(&style_art_03_hist_label_1_main_main_default, 7);
	lv_style_set_pad_right(&style_art_03_hist_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_art_03_hist_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_art_03_hist_label_1_main_main_default, 0);
	lv_obj_add_style(ui->Art_03_hist_label_1, &style_art_03_hist_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Art_03_hist_ta_1
	ui->Art_03_hist_ta_1 = lv_textarea_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_ta_1, 640, 15);
	lv_obj_set_size(ui->Art_03_hist_ta_1, 478, 41);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_ta_1, LV_SCROLLBAR_MODE_ON);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_ta_1_main_main_default
	static lv_style_t style_art_03_hist_ta_1_main_main_default;
	if (style_art_03_hist_ta_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_ta_1_main_main_default);
	else
		lv_style_init(&style_art_03_hist_ta_1_main_main_default);
	lv_style_set_radius(&style_art_03_hist_ta_1_main_main_default, 5);
	lv_style_set_bg_color(&style_art_03_hist_ta_1_main_main_default, lv_color_make(0xb8, 0x82, 0xab));
	lv_style_set_bg_grad_color(&style_art_03_hist_ta_1_main_main_default, lv_color_make(0x6b, 0x37, 0x86));
	lv_style_set_bg_grad_dir(&style_art_03_hist_ta_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_03_hist_ta_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_ta_1_main_main_default, 2);
	lv_style_set_shadow_color(&style_art_03_hist_ta_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_03_hist_ta_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_ta_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_ta_1_main_main_default, -5);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_ta_1_main_main_default, -3);
	lv_style_set_border_color(&style_art_03_hist_ta_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_03_hist_ta_1_main_main_default, 3);
	lv_style_set_border_opa(&style_art_03_hist_ta_1_main_main_default, 255);
	lv_style_set_text_color(&style_art_03_hist_ta_1_main_main_default, lv_color_make(0xfe, 0xfe, 0xfe));
	lv_style_set_text_font(&style_art_03_hist_ta_1_main_main_default, &lv_font_Acme_Regular_29);
	lv_style_set_text_letter_space(&style_art_03_hist_ta_1_main_main_default, 2);
	lv_style_set_text_align(&style_art_03_hist_ta_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_art_03_hist_ta_1_main_main_default, 4);
	lv_style_set_pad_right(&style_art_03_hist_ta_1_main_main_default, 4);
	lv_style_set_pad_top(&style_art_03_hist_ta_1_main_main_default, 4);
	lv_style_set_pad_bottom(&style_art_03_hist_ta_1_main_main_default, 4);
	lv_obj_add_style(ui->Art_03_hist_ta_1, &style_art_03_hist_ta_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_ta_1_main_scrollbar_default
	static lv_style_t style_art_03_hist_ta_1_main_scrollbar_default;
	if (style_art_03_hist_ta_1_main_scrollbar_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_ta_1_main_scrollbar_default);
	else
		lv_style_init(&style_art_03_hist_ta_1_main_scrollbar_default);
	lv_style_set_radius(&style_art_03_hist_ta_1_main_scrollbar_default, 0);
	lv_style_set_bg_color(&style_art_03_hist_ta_1_main_scrollbar_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_opa(&style_art_03_hist_ta_1_main_scrollbar_default, 255);
	lv_obj_add_style(ui->Art_03_hist_ta_1, &style_art_03_hist_ta_1_main_scrollbar_default, LV_PART_SCROLLBAR|LV_STATE_DEFAULT);
	lv_textarea_set_text(ui->Art_03_hist_ta_1,"HISTORY -  DIDARGANJ YAKSHI");

	//Write codes Art_03_hist_btn_1
	ui->Art_03_hist_btn_1 = lv_btn_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_btn_1, 514, 430);
	lv_obj_set_size(ui->Art_03_hist_btn_1, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_btn_1_main_main_default
	static lv_style_t style_art_03_hist_btn_1_main_main_default;
	if (style_art_03_hist_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_btn_1_main_main_default);
	else
		lv_style_init(&style_art_03_hist_btn_1_main_main_default);
	lv_style_set_radius(&style_art_03_hist_btn_1_main_main_default, 9);
	lv_style_set_bg_color(&style_art_03_hist_btn_1_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_03_hist_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_03_hist_btn_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_03_hist_btn_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_btn_1_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_03_hist_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_03_hist_btn_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_btn_1_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_btn_1_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_btn_1_main_main_default, 4);
	lv_style_set_border_color(&style_art_03_hist_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_03_hist_btn_1_main_main_default, 5);
	lv_style_set_border_opa(&style_art_03_hist_btn_1_main_main_default, 255);
	lv_style_set_text_color(&style_art_03_hist_btn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_03_hist_btn_1_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_03_hist_btn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_03_hist_btn_1, &style_art_03_hist_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_03_hist_btn_1_label = lv_label_create(ui->Art_03_hist_btn_1);
	lv_label_set_text(ui->Art_03_hist_btn_1_label, "BACK");
	lv_obj_set_style_pad_all(ui->Art_03_hist_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_03_hist_btn_1_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_03_hist_btn_2
	ui->Art_03_hist_btn_2 = lv_btn_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_btn_2, 925, 435);
	lv_obj_set_size(ui->Art_03_hist_btn_2, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_btn_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_btn_2_main_main_default
	static lv_style_t style_art_03_hist_btn_2_main_main_default;
	if (style_art_03_hist_btn_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_btn_2_main_main_default);
	else
		lv_style_init(&style_art_03_hist_btn_2_main_main_default);
	lv_style_set_radius(&style_art_03_hist_btn_2_main_main_default, 9);
	lv_style_set_bg_color(&style_art_03_hist_btn_2_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_03_hist_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_03_hist_btn_2_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_03_hist_btn_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_btn_2_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_03_hist_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_03_hist_btn_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_btn_2_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_btn_2_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_btn_2_main_main_default, 4);
	lv_style_set_border_color(&style_art_03_hist_btn_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_03_hist_btn_2_main_main_default, 5);
	lv_style_set_border_opa(&style_art_03_hist_btn_2_main_main_default, 255);
	lv_style_set_text_color(&style_art_03_hist_btn_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_03_hist_btn_2_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_03_hist_btn_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_03_hist_btn_2, &style_art_03_hist_btn_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_03_hist_btn_2_label = lv_label_create(ui->Art_03_hist_btn_2);
	lv_label_set_text(ui->Art_03_hist_btn_2_label, "1. STYLE");
	lv_obj_set_style_pad_all(ui->Art_03_hist_btn_2, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_03_hist_btn_2_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_03_hist_img_3
	ui->Art_03_hist_img_3 = lv_img_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_img_3, 926, 440);
	lv_obj_set_size(ui->Art_03_hist_img_3, 62, 60);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_img_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_img_3_main_main_default
	static lv_style_t style_art_03_hist_img_3_main_main_default;
	if (style_art_03_hist_img_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_img_3_main_main_default);
	else
		lv_style_init(&style_art_03_hist_img_3_main_main_default);
	lv_style_set_img_recolor(&style_art_03_hist_img_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_03_hist_img_3_main_main_default, 255);
	lv_style_set_img_opa(&style_art_03_hist_img_3_main_main_default, 255);
	lv_obj_add_style(ui->Art_03_hist_img_3, &style_art_03_hist_img_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_03_hist_img_3, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_03_hist_img_3,&_One_62x60);
	lv_img_set_pivot(ui->Art_03_hist_img_3, 50,50);
	lv_img_set_angle(ui->Art_03_hist_img_3, 0);

	//Write codes Art_03_hist_btn_4
	ui->Art_03_hist_btn_4 = lv_btn_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_btn_4, 512, 557);
	lv_obj_set_size(ui->Art_03_hist_btn_4, 335, 73);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_btn_4, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_btn_4_main_main_default
	static lv_style_t style_art_03_hist_btn_4_main_main_default;
	if (style_art_03_hist_btn_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_btn_4_main_main_default);
	else
		lv_style_init(&style_art_03_hist_btn_4_main_main_default);
	lv_style_set_radius(&style_art_03_hist_btn_4_main_main_default, 9);
	lv_style_set_bg_color(&style_art_03_hist_btn_4_main_main_default, lv_color_make(0x79, 0x1e, 0x6e));
	lv_style_set_bg_grad_color(&style_art_03_hist_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_bg_grad_dir(&style_art_03_hist_btn_4_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_art_03_hist_btn_4_main_main_default, 255);
	lv_style_set_shadow_width(&style_art_03_hist_btn_4_main_main_default, 3);
	lv_style_set_shadow_color(&style_art_03_hist_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_art_03_hist_btn_4_main_main_default, 255);
	lv_style_set_shadow_spread(&style_art_03_hist_btn_4_main_main_default, 3);
	lv_style_set_shadow_ofs_x(&style_art_03_hist_btn_4_main_main_default, 4);
	lv_style_set_shadow_ofs_y(&style_art_03_hist_btn_4_main_main_default, 4);
	lv_style_set_border_color(&style_art_03_hist_btn_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_art_03_hist_btn_4_main_main_default, 5);
	lv_style_set_border_opa(&style_art_03_hist_btn_4_main_main_default, 255);
	lv_style_set_text_color(&style_art_03_hist_btn_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_art_03_hist_btn_4_main_main_default, &lv_font_Acme_Regular_28);
	lv_style_set_text_align(&style_art_03_hist_btn_4_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_obj_add_style(ui->Art_03_hist_btn_4, &style_art_03_hist_btn_4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Art_03_hist_btn_4_label = lv_label_create(ui->Art_03_hist_btn_4);
	lv_label_set_text(ui->Art_03_hist_btn_4_label, "      NEXT ART");
	lv_obj_set_style_pad_all(ui->Art_03_hist_btn_4, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Art_03_hist_btn_4_label, LV_ALIGN_CENTER, 0, 0);

	//Write codes Art_03_hist_img_6
	ui->Art_03_hist_img_6 = lv_img_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_img_6, 529, 561);
	lv_obj_set_size(ui->Art_03_hist_img_6, 92, 70);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_img_6, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_img_6_main_main_default
	static lv_style_t style_art_03_hist_img_6_main_main_default;
	if (style_art_03_hist_img_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_img_6_main_main_default);
	else
		lv_style_init(&style_art_03_hist_img_6_main_main_default);
	lv_style_set_img_recolor(&style_art_03_hist_img_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_03_hist_img_6_main_main_default, 251);
	lv_style_set_img_opa(&style_art_03_hist_img_6_main_main_default, 255);
	lv_obj_add_style(ui->Art_03_hist_img_6, &style_art_03_hist_img_6_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_03_hist_img_6, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_03_hist_img_6,&_Next_92x70);
	lv_img_set_pivot(ui->Art_03_hist_img_6, 50,50);
	lv_img_set_angle(ui->Art_03_hist_img_6, 0);

	//Write codes Art_03_hist_video_1
	ui->Art_03_hist_video_1 = lv_video_create(ui->Art_03_hist_cont_1, 431, 477);
	lv_video_set_status(ui->Art_03_hist_video_1, 0);
#if LV_USE_GUIDER_SIMULATOR
	lv_video_set_src(ui->Art_03_hist_video_1,"");
#else
#endif
	lv_obj_set_pos(ui->Art_03_hist_video_1, 20, 85);
	lv_obj_set_size(ui->Art_03_hist_video_1, 431, 477);

	//Write codes Art_03_hist_img_7
	ui->Art_03_hist_img_7 = lv_img_create(ui->Art_03_hist_cont_1);
	lv_obj_set_pos(ui->Art_03_hist_img_7, 523, 433);
	lv_obj_set_size(ui->Art_03_hist_img_7, 79, 66);
	lv_obj_set_scrollbar_mode(ui->Art_03_hist_img_7, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_art_03_hist_img_7_main_main_default
	static lv_style_t style_art_03_hist_img_7_main_main_default;
	if (style_art_03_hist_img_7_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_art_03_hist_img_7_main_main_default);
	else
		lv_style_init(&style_art_03_hist_img_7_main_main_default);
	lv_style_set_img_recolor(&style_art_03_hist_img_7_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_art_03_hist_img_7_main_main_default, 254);
	lv_style_set_img_opa(&style_art_03_hist_img_7_main_main_default, 255);
	lv_obj_add_style(ui->Art_03_hist_img_7, &style_art_03_hist_img_7_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Art_03_hist_img_7, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Art_03_hist_img_7,&_Backthumb_79x66);
	lv_img_set_pivot(ui->Art_03_hist_img_7, 50,50);
	lv_img_set_angle(ui->Art_03_hist_img_7, 0);

	//Init events for screen
	events_init_Art_03_hist(ui);
}