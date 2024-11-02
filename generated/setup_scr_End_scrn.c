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


void setup_scr_End_scrn(lv_ui *ui){

	//Write codes End_scrn
	ui->End_scrn = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->End_scrn, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_main_main_default
	static lv_style_t style_end_scrn_main_main_default;
	if (style_end_scrn_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_main_main_default);
	else
		lv_style_init(&style_end_scrn_main_main_default);
	lv_style_set_bg_color(&style_end_scrn_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_end_scrn_main_main_default, 0);
	lv_obj_add_style(ui->End_scrn, &style_end_scrn_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes End_scrn_cont_1
	ui->End_scrn_cont_1 = lv_obj_create(ui->End_scrn);
	lv_obj_set_pos(ui->End_scrn_cont_1, 0, 0);
	lv_obj_set_size(ui->End_scrn_cont_1, 1280, 720);
	lv_obj_set_scrollbar_mode(ui->End_scrn_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_cont_1_main_main_default
	static lv_style_t style_end_scrn_cont_1_main_main_default;
	if (style_end_scrn_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_cont_1_main_main_default);
	else
		lv_style_init(&style_end_scrn_cont_1_main_main_default);
	lv_style_set_radius(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_bg_color(&style_end_scrn_cont_1_main_main_default, lv_color_make(0x13, 0x01, 0x14));
	lv_style_set_bg_grad_color(&style_end_scrn_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_end_scrn_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_end_scrn_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_end_scrn_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_end_scrn_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_end_scrn_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_border_width(&style_end_scrn_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_end_scrn_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_end_scrn_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_end_scrn_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->End_scrn_cont_1, &style_end_scrn_cont_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes End_scrn_label_1
	ui->End_scrn_label_1 = lv_label_create(ui->End_scrn_cont_1);
	lv_obj_set_pos(ui->End_scrn_label_1, 314, 375);
	lv_obj_set_size(ui->End_scrn_label_1, 664, 234);
	lv_obj_set_scrollbar_mode(ui->End_scrn_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->End_scrn_label_1, " YOU HAVE SUCCEFULLY COMPLETED THE MUSEUM TOUR \n\nClick Continue to Restart");
	lv_label_set_long_mode(ui->End_scrn_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_label_1_main_main_default
	static lv_style_t style_end_scrn_label_1_main_main_default;
	if (style_end_scrn_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_label_1_main_main_default);
	else
		lv_style_init(&style_end_scrn_label_1_main_main_default);
	lv_style_set_radius(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_end_scrn_label_1_main_main_default, lv_color_make(0x13, 0x01, 0x14));
	lv_style_set_bg_grad_color(&style_end_scrn_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_end_scrn_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_end_scrn_label_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_end_scrn_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_end_scrn_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_end_scrn_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_end_scrn_label_1_main_main_default, &lv_font_Alatsi_Regular_35);
	lv_style_set_text_letter_space(&style_end_scrn_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_end_scrn_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_end_scrn_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_end_scrn_label_1_main_main_default, 8);
	lv_style_set_pad_bottom(&style_end_scrn_label_1_main_main_default, 0);
	lv_obj_add_style(ui->End_scrn_label_1, &style_end_scrn_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes End_scrn_img_1
	ui->End_scrn_img_1 = lv_img_create(ui->End_scrn_cont_1);
	lv_obj_set_pos(ui->End_scrn_img_1, 462, 37);
	lv_obj_set_size(ui->End_scrn_img_1, 335, 329);
	lv_obj_set_scrollbar_mode(ui->End_scrn_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_img_1_main_main_default
	static lv_style_t style_end_scrn_img_1_main_main_default;
	if (style_end_scrn_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_img_1_main_main_default);
	else
		lv_style_init(&style_end_scrn_img_1_main_main_default);
	lv_style_set_img_recolor(&style_end_scrn_img_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_end_scrn_img_1_main_main_default, 0);
	lv_style_set_img_opa(&style_end_scrn_img_1_main_main_default, 255);
	lv_obj_add_style(ui->End_scrn_img_1, &style_end_scrn_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->End_scrn_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->End_scrn_img_1,&_Complete_335x329);
	lv_img_set_pivot(ui->End_scrn_img_1, 50,50);
	lv_img_set_angle(ui->End_scrn_img_1, 0);

	//Write codes End_scrn_btn_1
	ui->End_scrn_btn_1 = lv_btn_create(ui->End_scrn_cont_1);
	lv_obj_set_pos(ui->End_scrn_btn_1, 481, 573);
	lv_obj_set_size(ui->End_scrn_btn_1, 347, 86);
	lv_obj_set_scrollbar_mode(ui->End_scrn_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_btn_1_main_main_default
	static lv_style_t style_end_scrn_btn_1_main_main_default;
	if (style_end_scrn_btn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_btn_1_main_main_default);
	else
		lv_style_init(&style_end_scrn_btn_1_main_main_default);
	lv_style_set_radius(&style_end_scrn_btn_1_main_main_default, 9);
	lv_style_set_bg_color(&style_end_scrn_btn_1_main_main_default, lv_color_make(0x41, 0x60, 0x6E));
	lv_style_set_bg_grad_color(&style_end_scrn_btn_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_end_scrn_btn_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_end_scrn_btn_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_end_scrn_btn_1_main_main_default, 1);
	lv_style_set_shadow_color(&style_end_scrn_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_shadow_opa(&style_end_scrn_btn_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_end_scrn_btn_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_end_scrn_btn_1_main_main_default, 3);
	lv_style_set_shadow_ofs_y(&style_end_scrn_btn_1_main_main_default, 6);
	lv_style_set_border_color(&style_end_scrn_btn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_end_scrn_btn_1_main_main_default, 6);
	lv_style_set_border_opa(&style_end_scrn_btn_1_main_main_default, 255);
	lv_style_set_text_color(&style_end_scrn_btn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_end_scrn_btn_1_main_main_default, &lv_font_Acme_Regular_30);
	lv_style_set_text_align(&style_end_scrn_btn_1_main_main_default, LV_TEXT_ALIGN_LEFT);
	lv_obj_add_style(ui->End_scrn_btn_1, &style_end_scrn_btn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	ui->End_scrn_btn_1_label = lv_label_create(ui->End_scrn_btn_1);
	lv_label_set_text(ui->End_scrn_btn_1_label, "             CONTINUE");
	lv_obj_set_style_pad_all(ui->End_scrn_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_align(ui->End_scrn_btn_1_label, LV_ALIGN_LEFT_MID, 0, 0);

	//Write codes End_scrn_img_2
	ui->End_scrn_img_2 = lv_img_create(ui->End_scrn_cont_1);
	lv_obj_set_pos(ui->End_scrn_img_2, 709, 582);
	lv_obj_set_size(ui->End_scrn_img_2, 77, 67);
	lv_obj_set_scrollbar_mode(ui->End_scrn_img_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_end_scrn_img_2_main_main_default
	static lv_style_t style_end_scrn_img_2_main_main_default;
	if (style_end_scrn_img_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_end_scrn_img_2_main_main_default);
	else
		lv_style_init(&style_end_scrn_img_2_main_main_default);
	lv_style_set_img_recolor(&style_end_scrn_img_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_end_scrn_img_2_main_main_default, 255);
	lv_style_set_img_opa(&style_end_scrn_img_2_main_main_default, 255);
	lv_obj_add_style(ui->End_scrn_img_2, &style_end_scrn_img_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->End_scrn_img_2, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->End_scrn_img_2,&_Ok_Enter_77x67);
	lv_img_set_pivot(ui->End_scrn_img_2, 50,50);
	lv_img_set_angle(ui->End_scrn_img_2, 0);

	//Init events for screen
	events_init_End_scrn(ui);
}