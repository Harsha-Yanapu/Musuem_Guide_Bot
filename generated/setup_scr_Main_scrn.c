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


void setup_scr_Main_scrn(lv_ui *ui){

	//Write codes Main_scrn
	ui->Main_scrn = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->Main_scrn, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_main_main_default
	static lv_style_t style_main_scrn_main_main_default;
	if (style_main_scrn_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_main_main_default);
	else
		lv_style_init(&style_main_scrn_main_main_default);
	lv_style_set_bg_color(&style_main_scrn_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_main_scrn_main_main_default, 0);
	lv_obj_add_style(ui->Main_scrn, &style_main_scrn_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes Main_scrn_img_1
	ui->Main_scrn_img_1 = lv_img_create(ui->Main_scrn);
	lv_obj_set_pos(ui->Main_scrn_img_1, 0, 0);
	lv_obj_set_size(ui->Main_scrn_img_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->Main_scrn_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_img_1_main_main_default
	static lv_style_t style_main_scrn_img_1_main_main_default;
	if (style_main_scrn_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_img_1_main_main_default);
	else
		lv_style_init(&style_main_scrn_img_1_main_main_default);
	lv_style_set_img_recolor(&style_main_scrn_img_1_main_main_default, lv_color_make(0xff, 0x00, 0xb2));
	lv_style_set_img_recolor_opa(&style_main_scrn_img_1_main_main_default, 46);
	lv_style_set_img_opa(&style_main_scrn_img_1_main_main_default, 255);
	lv_obj_add_style(ui->Main_scrn_img_1, &style_main_scrn_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Main_scrn_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Main_scrn_img_1,&_background_1280x720);
	lv_img_set_pivot(ui->Main_scrn_img_1, 50,50);
	lv_img_set_angle(ui->Main_scrn_img_1, 0);

	//Write codes Main_scrn_imgbtn_1
	ui->Main_scrn_imgbtn_1 = lv_imgbtn_create(ui->Main_scrn);
	lv_obj_set_pos(ui->Main_scrn_imgbtn_1, 26, 17);
	lv_obj_set_size(ui->Main_scrn_imgbtn_1, 132, 124);
	lv_obj_set_scrollbar_mode(ui->Main_scrn_imgbtn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_imgbtn_1_main_main_default
	static lv_style_t style_main_scrn_imgbtn_1_main_main_default;
	if (style_main_scrn_imgbtn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_imgbtn_1_main_main_default);
	else
		lv_style_init(&style_main_scrn_imgbtn_1_main_main_default);
	lv_style_set_shadow_width(&style_main_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_main_scrn_imgbtn_1_main_main_default, lv_color_make(0x04, 0x0f, 0x18));
	lv_style_set_shadow_opa(&style_main_scrn_imgbtn_1_main_main_default, 246);
	lv_style_set_shadow_spread(&style_main_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_main_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_main_scrn_imgbtn_1_main_main_default, 0);
	lv_style_set_text_color(&style_main_scrn_imgbtn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_main_scrn_imgbtn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_main_scrn_imgbtn_1_main_main_default, lv_color_make(0xff, 0x00, 0xb8));
	lv_style_set_img_recolor_opa(&style_main_scrn_imgbtn_1_main_main_default, 17);
	lv_style_set_img_opa(&style_main_scrn_imgbtn_1_main_main_default, 255);
	lv_obj_add_style(ui->Main_scrn_imgbtn_1, &style_main_scrn_imgbtn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_main_scrn_imgbtn_1_main_main_pressed
	static lv_style_t style_main_scrn_imgbtn_1_main_main_pressed;
	if (style_main_scrn_imgbtn_1_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_imgbtn_1_main_main_pressed);
	else
		lv_style_init(&style_main_scrn_imgbtn_1_main_main_pressed);
	lv_style_set_shadow_width(&style_main_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_color(&style_main_scrn_imgbtn_1_main_main_pressed, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_main_scrn_imgbtn_1_main_main_pressed, 255);
	lv_style_set_shadow_spread(&style_main_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_ofs_x(&style_main_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_shadow_ofs_y(&style_main_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_text_color(&style_main_scrn_imgbtn_1_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_img_recolor(&style_main_scrn_imgbtn_1_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_main_scrn_imgbtn_1_main_main_pressed, 0);
	lv_style_set_img_opa(&style_main_scrn_imgbtn_1_main_main_pressed, 255);
	lv_obj_add_style(ui->Main_scrn_imgbtn_1, &style_main_scrn_imgbtn_1_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_main_scrn_imgbtn_1_main_main_checked
	static lv_style_t style_main_scrn_imgbtn_1_main_main_checked;
	if (style_main_scrn_imgbtn_1_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_imgbtn_1_main_main_checked);
	else
		lv_style_init(&style_main_scrn_imgbtn_1_main_main_checked);
	lv_style_set_shadow_width(&style_main_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_color(&style_main_scrn_imgbtn_1_main_main_checked, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_main_scrn_imgbtn_1_main_main_checked, 255);
	lv_style_set_shadow_spread(&style_main_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_ofs_x(&style_main_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_shadow_ofs_y(&style_main_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_text_color(&style_main_scrn_imgbtn_1_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_img_recolor(&style_main_scrn_imgbtn_1_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_main_scrn_imgbtn_1_main_main_checked, 0);
	lv_style_set_img_opa(&style_main_scrn_imgbtn_1_main_main_checked, 255);
	lv_obj_add_style(ui->Main_scrn_imgbtn_1, &style_main_scrn_imgbtn_1_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->Main_scrn_imgbtn_1, LV_IMGBTN_STATE_RELEASED, NULL, &_Help_alpha_132x124, NULL);
	lv_imgbtn_set_src(ui->Main_scrn_imgbtn_1, LV_IMGBTN_STATE_PRESSED, NULL, &_Help_alpha_132x124, NULL);

	//Write codes Main_scrn_ta_1
	ui->Main_scrn_ta_1 = lv_textarea_create(ui->Main_scrn);
	lv_obj_set_pos(ui->Main_scrn_ta_1, 358, 210);
	lv_obj_set_size(ui->Main_scrn_ta_1, 550, 55);
	lv_obj_set_scrollbar_mode(ui->Main_scrn_ta_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_ta_1_main_main_default
	static lv_style_t style_main_scrn_ta_1_main_main_default;
	if (style_main_scrn_ta_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_ta_1_main_main_default);
	else
		lv_style_init(&style_main_scrn_ta_1_main_main_default);
	lv_style_set_radius(&style_main_scrn_ta_1_main_main_default, 4);
	lv_style_set_bg_color(&style_main_scrn_ta_1_main_main_default, lv_color_make(0x6c, 0x35, 0x65));
	lv_style_set_bg_grad_color(&style_main_scrn_ta_1_main_main_default, lv_color_make(0x45, 0x45, 0xb0));
	lv_style_set_bg_grad_dir(&style_main_scrn_ta_1_main_main_default, LV_GRAD_DIR_HOR);
	lv_style_set_bg_opa(&style_main_scrn_ta_1_main_main_default, 107);
	lv_style_set_shadow_width(&style_main_scrn_ta_1_main_main_default, 6);
	lv_style_set_shadow_color(&style_main_scrn_ta_1_main_main_default, lv_color_make(0x09, 0x0e, 0x0c));
	lv_style_set_shadow_opa(&style_main_scrn_ta_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_main_scrn_ta_1_main_main_default, 6);
	lv_style_set_shadow_ofs_x(&style_main_scrn_ta_1_main_main_default, 2);
	lv_style_set_shadow_ofs_y(&style_main_scrn_ta_1_main_main_default, 5);
	lv_style_set_border_color(&style_main_scrn_ta_1_main_main_default, lv_color_make(0x3a, 0x55, 0x9c));
	lv_style_set_border_width(&style_main_scrn_ta_1_main_main_default, 3);
	lv_style_set_border_opa(&style_main_scrn_ta_1_main_main_default, 43);
	lv_style_set_text_color(&style_main_scrn_ta_1_main_main_default, lv_color_make(0x2f, 0x38, 0x53));
	lv_style_set_text_font(&style_main_scrn_ta_1_main_main_default, &lv_font_Acme_Regular_40);
	lv_style_set_text_letter_space(&style_main_scrn_ta_1_main_main_default, 2);
	lv_style_set_text_align(&style_main_scrn_ta_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_main_scrn_ta_1_main_main_default, 4);
	lv_style_set_pad_right(&style_main_scrn_ta_1_main_main_default, 4);
	lv_style_set_pad_top(&style_main_scrn_ta_1_main_main_default, 4);
	lv_style_set_pad_bottom(&style_main_scrn_ta_1_main_main_default, 4);
	lv_obj_add_style(ui->Main_scrn_ta_1, &style_main_scrn_ta_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_ta_1_main_scrollbar_default
	static lv_style_t style_main_scrn_ta_1_main_scrollbar_default;
	if (style_main_scrn_ta_1_main_scrollbar_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_ta_1_main_scrollbar_default);
	else
		lv_style_init(&style_main_scrn_ta_1_main_scrollbar_default);
	lv_style_set_radius(&style_main_scrn_ta_1_main_scrollbar_default, 0);
	lv_style_set_bg_color(&style_main_scrn_ta_1_main_scrollbar_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_opa(&style_main_scrn_ta_1_main_scrollbar_default, 255);
	lv_obj_add_style(ui->Main_scrn_ta_1, &style_main_scrn_ta_1_main_scrollbar_default, LV_PART_SCROLLBAR|LV_STATE_DEFAULT);
	lv_textarea_set_text(ui->Main_scrn_ta_1,"MUSEUM GUIDE ROBOT ");

	//Write codes Main_scrn_btn_1
	ui->Main_scrn_btn_1 = lv_btn_create(ui->Main_scrn);
	lv_obj_set_pos(ui->Main_scrn_btn_1, 468, 547);
	lv_obj_set_size(ui->Main_scrn_btn_1, 344, 103);
	lv_obj_set_scrollbar_mode(ui->Main_scrn_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_btn_1_main_main_default
	static lv_style_t style_main_scrn_btn_1_main_main_default;
	if (style_main_scrn_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_btn_1_main_main_default);
	else
		lv_style_init(&style_main_scrn_btn_1_main_main_default);
	lv_style_set_radius(&style_main_scrn_btn_1_main_main_default, 9);
	lv_style_set_bg_color(&style_main_scrn_btn_1_main_main_default, lv_color_make(0x41, 0x60, 0x6e));
	lv_style_set_bg_grad_color(&style_main_scrn_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_main_scrn_btn_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_main_scrn_btn_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_main_scrn_btn_1_main_main_default, 1);
	lv_style_set_shadow_color(&style_main_scrn_btn_1_main_main_default, lv_color_make(0x06, 0x15, 0x21));
	lv_style_set_shadow_opa(&style_main_scrn_btn_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_main_scrn_btn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_main_scrn_btn_1_main_main_default, 3);
	lv_style_set_shadow_ofs_y(&style_main_scrn_btn_1_main_main_default, 6);
	lv_style_set_border_color(&style_main_scrn_btn_1_main_main_default, lv_color_make(0x0c, 0x18, 0x21));
	lv_style_set_border_width(&style_main_scrn_btn_1_main_main_default, 6);
	lv_style_set_border_opa(&style_main_scrn_btn_1_main_main_default, 255);
	lv_style_set_text_color(&style_main_scrn_btn_1_main_main_default, lv_color_make(0xd6, 0xe8, 0xac));
	lv_style_set_text_font(&style_main_scrn_btn_1_main_main_default, &lv_font_Acme_Regular_26);
	lv_style_set_text_align(&style_main_scrn_btn_1_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_obj_add_style(ui->Main_scrn_btn_1, &style_main_scrn_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->Main_scrn_btn_1_label = lv_label_create(ui->Main_scrn_btn_1);
	lv_label_set_text(ui->Main_scrn_btn_1_label, "      START EXPLORING ");
	lv_obj_set_style_pad_all(ui->Main_scrn_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->Main_scrn_btn_1_label, LV_ALIGN_LEFT_MID, 0, 0);

	//Write codes Main_scrn_img_2
	ui->Main_scrn_img_2 = lv_img_create(ui->Main_scrn);
	lv_obj_set_pos(ui->Main_scrn_img_2, 707, 558);
	lv_obj_set_size(ui->Main_scrn_img_2, 83, 78);
	lv_obj_set_scrollbar_mode(ui->Main_scrn_img_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_main_scrn_img_2_main_main_default
	static lv_style_t style_main_scrn_img_2_main_main_default;
	if (style_main_scrn_img_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_main_scrn_img_2_main_main_default);
	else
		lv_style_init(&style_main_scrn_img_2_main_main_default);
	lv_style_set_img_recolor(&style_main_scrn_img_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_main_scrn_img_2_main_main_default, 232);
	lv_style_set_img_opa(&style_main_scrn_img_2_main_main_default, 255);
	lv_obj_add_style(ui->Main_scrn_img_2, &style_main_scrn_img_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->Main_scrn_img_2, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->Main_scrn_img_2,&_Ok_Enter_83x78);
	lv_img_set_pivot(ui->Main_scrn_img_2, 50,50);
	lv_img_set_angle(ui->Main_scrn_img_2, 0);

	//Init events for screen
	events_init_Main_scrn(ui);
}