/*
 * Copyright 2024 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "events_init.h"
#include <stdio.h>
#include "lvgl.h"

void events_init(lv_ui *ui)
{
}

void video_play(lv_ui *ui)
{

}

static void Main_scrn_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_RELEASED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Help_scrn_del == true)
				setup_scr_Help_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.Help_scrn, LV_SCR_LOAD_ANIM_MOVE_RIGHT, 100, 100, false);
			guider_ui.Main_scrn_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Main_scrn_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_del == true)
				setup_scr_Art_01(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01, LV_SCR_LOAD_ANIM_MOVE_TOP, 100, 100, false);
			guider_ui.Main_scrn_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Main_scrn(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Main_scrn_imgbtn_1, Main_scrn_imgbtn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Main_scrn_btn_1, Main_scrn_btn_1_event_handler, LV_EVENT_ALL, ui);
}

static void Help_scrn_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_RELEASED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Main_scrn_del == true)
				setup_scr_Main_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.Main_scrn, LV_SCR_LOAD_ANIM_MOVE_LEFT, 100, 100, false);
			guider_ui.Help_scrn_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Help_scrn(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Help_scrn_imgbtn_1, Help_scrn_imgbtn_1_event_handler, LV_EVENT_ALL, ui);
}

static void Art_01_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_hist_del == true)
				setup_scr_Art_01_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_decep_del == true)
				setup_scr_Art_01_decep(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_decep, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_inter_del == true)
				setup_scr_Art_01_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_1_del == true)
				setup_scr_Load_scrn_1(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_1, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_01(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_01_btn_1, Art_01_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_btn_2, Art_01_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_btn_3, Art_01_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_btn_4, Art_01_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_01_hist_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_del == true)
				setup_scr_Art_01(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_hist_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_decep_del == true)
				setup_scr_Art_01_decep(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_decep, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_hist_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_inter_del == true)
				setup_scr_Art_01_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_hist_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_1_del == true)
				setup_scr_Load_scrn_1(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_1, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_01_hist(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_01_hist_btn_1, Art_01_hist_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_hist_btn_2, Art_01_hist_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_hist_btn_3, Art_01_hist_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_hist_btn_4, Art_01_hist_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_01_decep_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_del == true)
				setup_scr_Art_01(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_decep_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_decep_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_hist_del == true)
				setup_scr_Art_01_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_decep_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_decep_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_inter_del == true)
				setup_scr_Art_01_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_decep_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_decep_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_1_del == true)
				setup_scr_Load_scrn_1(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_1, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_decep_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_01_decep(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_01_decep_btn_1, Art_01_decep_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_decep_btn_2, Art_01_decep_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_decep_btn_3, Art_01_decep_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_decep_btn_4, Art_01_decep_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_01_inter_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_del == true)
				setup_scr_Art_01(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_inter_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_hist_del == true)
				setup_scr_Art_01_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_inter_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_01_decep_del == true)
				setup_scr_Art_01_decep(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_01_decep, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_01_inter_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_1_del == true)
				setup_scr_Load_scrn_1(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_1, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_01_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_01_inter(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_01_inter_btn_1, Art_01_inter_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_inter_btn_2, Art_01_inter_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_inter_btn_3, Art_01_inter_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_01_inter_btn_4, Art_01_inter_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_02_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_des_del == true)
				setup_scr_Art_02_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_inter_del == true)
				setup_scr_Art_02_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_2_del == true)
				setup_scr_Load_scrn_2(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_2, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_02(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_02_btn_2, Art_02_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_btn_3, Art_02_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_btn_4, Art_02_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_02_hist_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_del == true)
				setup_scr_Art_02(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_hist_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_des_del == true)
				setup_scr_Art_02_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_hist_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_inter_del == true)
				setup_scr_Art_02_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_hist_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_2_del == true)
				setup_scr_Load_scrn_2(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_2, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_02_hist(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_02_hist_btn_1, Art_02_hist_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_hist_btn_2, Art_02_hist_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_hist_btn_3, Art_02_hist_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_hist_btn_4, Art_02_hist_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_02_des_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_del == true)
				setup_scr_Art_02(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_des_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_hist_del == true)
				setup_scr_Art_02_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_des_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_inter_del == true)
				setup_scr_Art_02_inter(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_inter, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_des_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_2_del == true)
				setup_scr_Load_scrn_2(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_2, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_02_des(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_02_des_btn_1, Art_02_des_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_des_btn_2, Art_02_des_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_des_btn_3, Art_02_des_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_des_btn_4, Art_02_des_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_02_inter_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_del == true)
				setup_scr_Art_02(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_inter_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_hist_del == true)
				setup_scr_Art_02_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_inter_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_des_del == true)
				setup_scr_Art_02_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_02_inter_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_2_del == true)
				setup_scr_Load_scrn_2(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_2, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_02_inter_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_02_inter(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_02_inter_btn_1, Art_02_inter_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_inter_btn_2, Art_02_inter_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_inter_btn_3, Art_02_inter_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_02_inter_btn_4, Art_02_inter_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_03_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_hist_del == true)
				setup_scr_Art_03_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_style_del == true)
				setup_scr_Art_03_style(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03_style, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_3_del == true)
				setup_scr_Load_scrn_3(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_3, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_03(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_03_btn_1, Art_03_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_btn_2, Art_03_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_btn_4, Art_03_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_03_hist_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_del == true)
				setup_scr_Art_03(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_hist_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_style_del == true)
				setup_scr_Art_03_style(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03_style, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_hist_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_3_del == true)
				setup_scr_Load_scrn_3(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_3, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_03_hist(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_03_hist_btn_1, Art_03_hist_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_hist_btn_2, Art_03_hist_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_hist_btn_4, Art_03_hist_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_03_style_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_del == true)
				setup_scr_Art_03(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_style_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_hist_del == true)
				setup_scr_Art_03_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_03_style_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_3_del == true)
				setup_scr_Load_scrn_3(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_3, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_03_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_03_style(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_03_style_btn_1, Art_03_style_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_style_btn_2, Art_03_style_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_03_style_btn_4, Art_03_style_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_04_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_hist_del == true)
				setup_scr_Art_04_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_style_del == true)
				setup_scr_Art_04_style(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_style, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_4_del == true)
				setup_scr_Load_scrn_4(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_4, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_btn_5_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_des_del == true)
				setup_scr_Art_04_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_04(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_04_btn_1, Art_04_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_btn_2, Art_04_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_btn_4, Art_04_btn_4_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_btn_5, Art_04_btn_5_event_handler, LV_EVENT_ALL, ui);
}

static void Art_04_hist_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_del == true)
				setup_scr_Art_04(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_hist_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_style_del == true)
				setup_scr_Art_04_style(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_style, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_hist_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_des_del == true)
				setup_scr_Art_04_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_hist_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_4_del == true)
				setup_scr_Load_scrn_4(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_4, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_04_hist(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_04_hist_btn_1, Art_04_hist_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_hist_btn_2, Art_04_hist_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_hist_btn_3, Art_04_hist_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_hist_btn_4, Art_04_hist_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_04_style_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_del == true)
				setup_scr_Art_04(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_style_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_hist_del == true)
				setup_scr_Art_04_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_hist, LV_SCR_LOAD_ANIM_NONE, 100, 100, false);
			guider_ui.Art_04_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_style_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_des_del == true)
				setup_scr_Art_04_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_style_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_4_del == true)
				setup_scr_Load_scrn_4(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_4, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_style_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_04_style(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_04_style_btn_1, Art_04_style_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_style_btn_2, Art_04_style_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_style_btn_3, Art_04_style_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_style_btn_4, Art_04_style_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_04_des_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_del == true)
				setup_scr_Art_04(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_des_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_hist_del == true)
				setup_scr_Art_04_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_des_btn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_style_del == true)
				setup_scr_Art_04_style(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04_style, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_04_des_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Load_scrn_4_del == true)
				setup_scr_Load_scrn_4(&guider_ui);
			lv_scr_load_anim(guider_ui.Load_scrn_4, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_04_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_04_des(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_04_des_btn_1, Art_04_des_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_des_btn_2, Art_04_des_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_des_btn_3, Art_04_des_btn_3_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_04_des_btn_4, Art_04_des_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_05_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_hist_del == true)
				setup_scr_Art_05_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_des_del == true)
				setup_scr_Art_05_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.End_scrn_del == true)
				setup_scr_End_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.End_scrn, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_05(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_05_btn_1, Art_05_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_btn_2, Art_05_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_btn_4, Art_05_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_05_hist_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_del == true)
				setup_scr_Art_05(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_hist_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_des_del == true)
				setup_scr_Art_05_des(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05_des, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_hist_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.End_scrn_del == true)
				setup_scr_End_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.End_scrn, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_hist_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_05_hist(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_05_hist_btn_1, Art_05_hist_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_hist_btn_2, Art_05_hist_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_hist_btn_4, Art_05_hist_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Art_05_des_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_del == true)
				setup_scr_Art_05(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_des_btn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_hist_del == true)
				setup_scr_Art_05_hist(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05_hist, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

static void Art_05_des_btn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.End_scrn_del == true)
				setup_scr_End_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.End_scrn, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.Art_05_des_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Art_05_des(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Art_05_des_btn_1, Art_05_des_btn_1_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_des_btn_2, Art_05_des_btn_2_event_handler, LV_EVENT_ALL, ui);
	lv_obj_add_event_cb(ui->Art_05_des_btn_4, Art_05_des_btn_4_event_handler, LV_EVENT_ALL, ui);
}

static void Load_scrn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_SCREEN_LOADED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_02_del == true)
				setup_scr_Art_02(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_02, LV_SCR_LOAD_ANIM_FADE_ON, 4000, 100, false);
			guider_ui.Load_scrn_1_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Load_scrn_1(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Load_scrn_1, Load_scrn_1_event_handler, LV_EVENT_ALL, ui);
}

static void End_scrn_btn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_CLICKED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Main_scrn_del == true)
				setup_scr_Main_scrn(&guider_ui);
			lv_scr_load_anim(guider_ui.Main_scrn, LV_SCR_LOAD_ANIM_FADE_ON, 100, 100, false);
			guider_ui.End_scrn_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_End_scrn(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->End_scrn_btn_1, End_scrn_btn_1_event_handler, LV_EVENT_ALL, ui);
}

static void Load_scrn_2_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_SCREEN_LOADED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_03_del == true)
				setup_scr_Art_03(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_03, LV_SCR_LOAD_ANIM_FADE_ON, 4000, 100, false);
			guider_ui.Load_scrn_2_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Load_scrn_2(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Load_scrn_2, Load_scrn_2_event_handler, LV_EVENT_ALL, ui);
}

static void Load_scrn_3_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_SCREEN_LOADED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_04_del == true)
				setup_scr_Art_04(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_04, LV_SCR_LOAD_ANIM_FADE_ON, 4000, 100, false);
			guider_ui.Load_scrn_3_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Load_scrn_3(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Load_scrn_3, Load_scrn_3_event_handler, LV_EVENT_ALL, ui);
}

static void Load_scrn_4_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_SCREEN_LOADED:
	{
		lv_obj_t * act_scr = lv_scr_act();
		lv_disp_t * d = lv_obj_get_disp(act_scr);
		if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr))
		{
			if (guider_ui.Art_05_del == true)
				setup_scr_Art_05(&guider_ui);
			lv_scr_load_anim(guider_ui.Art_05, LV_SCR_LOAD_ANIM_FADE_ON, 4000, 100, false);
			guider_ui.Load_scrn_4_del = false;
		}
	}
		break;
	default:
		break;
	}
}

void events_init_Load_scrn_4(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->Load_scrn_4, Load_scrn_4_event_handler, LV_EVENT_ALL, ui);
}
