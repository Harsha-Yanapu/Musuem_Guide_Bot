/*
 * Copyright 2024 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"


void init_scr_del_flag(lv_ui *ui){
	ui->Main_scrn_del = true;
	ui->Help_scrn_del = true;
	ui->Art_01_del = true;
	ui->Art_01_hist_del = true;
	ui->Art_01_decep_del = true;
	ui->Art_01_inter_del = true;
	ui->Art_02_del = true;
	ui->Art_02_hist_del = true;
	ui->Art_02_des_del = true;
	ui->Art_02_inter_del = true;
	ui->Art_03_del = true;
	ui->Art_03_hist_del = true;
	ui->Art_03_style_del = true;
	ui->Art_04_del = true;
	ui->Art_04_hist_del = true;
	ui->Art_04_style_del = true;
	ui->Art_04_des_del = true;
	ui->Art_05_del = true;
	ui->Art_05_hist_del = true;
	ui->Art_05_des_del = true;
	ui->Load_scrn_1_del = true;
	ui->End_scrn_del = true;
	ui->Load_scrn_2_del = true;
	ui->Load_scrn_3_del = true;
	ui->Load_scrn_4_del = true;
}

void setup_ui(lv_ui *ui){
	init_scr_del_flag(ui);
	setup_scr_Main_scrn(ui);
	lv_scr_load(ui->Main_scrn);
}
