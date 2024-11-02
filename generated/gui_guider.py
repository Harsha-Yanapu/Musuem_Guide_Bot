# Copyright 2022 NXP
# SPDX-License-Identifier: MIT
# The auto-generated can only be used on NXP devices

import SDL
import utime as time
import usys as sys
import lvgl as lv
import lodepng as png
import ustruct

lv.init()
SDL.init(w=1280,h=720)

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(1280*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 1280
disp_drv.ver_res = 720
disp_drv.register()

# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()

# Below: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

COLOR_SIZE = lv.color_t.__SIZE__
COLOR_IS_SWAPPED = hasattr(lv.color_t().ch,'green_h')

class lodepng_error(RuntimeError):
    def __init__(self, err):
        if type(err) is int:
            super().__init__(png.error_text(err))
        else:
            super().__init__(err)

# Parse PNG file header
# Taken from https://github.com/shibukawa/imagesize_py/blob/ffef30c1a4715c5acf90e8945ceb77f4a2ed2d45/imagesize.py#L63-L85

def get_png_info(decoder, src, header):
    # Only handle variable image types

    if lv.img.src_get_type(src) != lv.img.SRC.VARIABLE:
        return lv.RES.INV

    data = lv.img_dsc_t.__cast__(src).data
    if data == None:
        return lv.RES.INV

    png_header = bytes(data.__dereference__(24))

    if png_header.startswith(b'\211PNG\r\n\032\n'):
        if png_header[12:16] == b'IHDR':
            start = 16
        # Maybe this is for an older PNG version.
        else:
            start = 8
        try:
            width, height = ustruct.unpack(">LL", png_header[start:start+8])
        except ustruct.error:
            return lv.RES.INV
    else:
        return lv.RES.INV

    header.always_zero = 0
    header.w = width
    header.h = height
    header.cf = lv.img.CF.TRUE_COLOR_ALPHA

    return lv.RES.OK

def convert_rgba8888_to_bgra8888(img_view):
    for i in range(0, len(img_view), lv.color_t.__SIZE__):
        ch = lv.color_t.__cast__(img_view[i:i]).ch
        ch.red, ch.blue = ch.blue, ch.red

# Read and parse PNG file

def open_png(decoder, dsc):
    img_dsc = lv.img_dsc_t.__cast__(dsc.src)
    png_data = img_dsc.data
    png_size = img_dsc.data_size
    png_decoded = png.C_Pointer()
    png_width = png.C_Pointer()
    png_height = png.C_Pointer()
    error = png.decode32(png_decoded, png_width, png_height, png_data, png_size)
    if error:
        raise lodepng_error(error)
    img_size = png_width.int_val * png_height.int_val * 4
    img_data = png_decoded.ptr_val
    img_view = img_data.__dereference__(img_size)

    if COLOR_SIZE == 4:
        convert_rgba8888_to_bgra8888(img_view)
    else:
        raise lodepng_error("Error: Color mode not supported yet!")

    dsc.img_data = img_data
    return lv.RES.OK

# Above: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)



# create Main_scrn
Main_scrn = lv.obj()
Main_scrn.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_main_scrn_main_main_default
style_main_scrn_main_main_default = lv.style_t()
style_main_scrn_main_main_default.init()
style_main_scrn_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_main_scrn_main_main_default.set_bg_opa(0)

# add style for Main_scrn
Main_scrn.add_style(style_main_scrn_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Main_scrn_img_1
Main_scrn_img_1 = lv.img(Main_scrn)
Main_scrn_img_1.set_pos(int(0),int(0))
Main_scrn_img_1.set_size(1280,720)
Main_scrn_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Main_scrn_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Main_scrn_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Main_scrn_img_1_img = lv.img_dsc_t({
  'data_size': len(Main_scrn_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Main_scrn_img_1_img_data
})

Main_scrn_img_1.set_src(Main_scrn_img_1_img)
Main_scrn_img_1.set_pivot(50,50)
Main_scrn_img_1.set_angle(0)
# create style style_main_scrn_img_1_main_main_default
style_main_scrn_img_1_main_main_default = lv.style_t()
style_main_scrn_img_1_main_main_default.init()
style_main_scrn_img_1_main_main_default.set_img_recolor(lv.color_make(0xff,0x00,0xb2))
style_main_scrn_img_1_main_main_default.set_img_recolor_opa(46)
style_main_scrn_img_1_main_main_default.set_img_opa(255)

# add style for Main_scrn_img_1
Main_scrn_img_1.add_style(style_main_scrn_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Main_scrn_imgbtn_1
Main_scrn_imgbtn_1 = lv.imgbtn(Main_scrn)
Main_scrn_imgbtn_1.set_pos(int(26),int(17))
Main_scrn_imgbtn_1.set_size(132,124)
Main_scrn_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-974703201.png','rb') as f:
        Main_scrn_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-974703201.png')
    sys.exit()

Main_scrn_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(Main_scrn_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 132, 'h': 124, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Main_scrn_imgbtn_1_imgReleased_data
})
Main_scrn_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, None, Main_scrn_imgbtn_1_imgReleased, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-974703201.png','rb') as f:
        Main_scrn_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-974703201.png')
    sys.exit()

Main_scrn_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(Main_scrn_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 132, 'h': 124, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Main_scrn_imgbtn_1_imgPressed_data
})
Main_scrn_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, None, Main_scrn_imgbtn_1_imgPressed, None)




# create style style_main_scrn_imgbtn_1_main_main_default
style_main_scrn_imgbtn_1_main_main_default = lv.style_t()
style_main_scrn_imgbtn_1_main_main_default.init()
style_main_scrn_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_main_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_Acme_Regular_37)
except AttributeError:
    try:
        style_main_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_37)
    except AttributeError:
        style_main_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_main_scrn_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_main_scrn_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0xff,0x00,0xb8))
style_main_scrn_imgbtn_1_main_main_default.set_img_recolor_opa(17)
style_main_scrn_imgbtn_1_main_main_default.set_img_opa(255)

# add style for Main_scrn_imgbtn_1
Main_scrn_imgbtn_1.add_style(style_main_scrn_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_main_scrn_imgbtn_1_main_main_pressed
style_main_scrn_imgbtn_1_main_main_pressed = lv.style_t()
style_main_scrn_imgbtn_1_main_main_pressed.init()
style_main_scrn_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_main_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserratMedium_12)
except AttributeError:
    try:
        style_main_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_main_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_main_scrn_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_main_scrn_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_main_scrn_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for Main_scrn_imgbtn_1
Main_scrn_imgbtn_1.add_style(style_main_scrn_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_main_scrn_imgbtn_1_main_main_checked
style_main_scrn_imgbtn_1_main_main_checked = lv.style_t()
style_main_scrn_imgbtn_1_main_main_checked.init()
style_main_scrn_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_main_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserratMedium_12)
except AttributeError:
    try:
        style_main_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_main_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_main_scrn_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_main_scrn_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_main_scrn_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for Main_scrn_imgbtn_1
Main_scrn_imgbtn_1.add_style(style_main_scrn_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)


# create Main_scrn_ta_1
Main_scrn_ta_1 = lv.textarea(Main_scrn)
Main_scrn_ta_1.set_pos(int(358),int(210))
Main_scrn_ta_1.set_size(550,55)
Main_scrn_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Main_scrn_ta_1.set_text("MUSEUM GUIDE ROBOT ")


# create style style_main_scrn_ta_1_main_main_default
style_main_scrn_ta_1_main_main_default = lv.style_t()
style_main_scrn_ta_1_main_main_default.init()
style_main_scrn_ta_1_main_main_default.set_radius(4)
style_main_scrn_ta_1_main_main_default.set_bg_color(lv.color_make(0x6c,0x35,0x65))
style_main_scrn_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x45,0x45,0xb0))
style_main_scrn_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_main_scrn_ta_1_main_main_default.set_bg_opa(107)
style_main_scrn_ta_1_main_main_default.set_shadow_width(6)
style_main_scrn_ta_1_main_main_default.set_shadow_color(lv.color_make(0x09,0x0e,0x0c))
style_main_scrn_ta_1_main_main_default.set_shadow_opa(255)
style_main_scrn_ta_1_main_main_default.set_shadow_spread(6)
style_main_scrn_ta_1_main_main_default.set_shadow_ofs_x(2)
style_main_scrn_ta_1_main_main_default.set_shadow_ofs_y(5)
style_main_scrn_ta_1_main_main_default.set_border_color(lv.color_make(0x3a,0x55,0x9c))
style_main_scrn_ta_1_main_main_default.set_border_width(3)
style_main_scrn_ta_1_main_main_default.set_border_opa(43)
style_main_scrn_ta_1_main_main_default.set_text_color(lv.color_make(0x2f,0x38,0x53))
try:
    style_main_scrn_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_40)
except AttributeError:
    try:
        style_main_scrn_ta_1_main_main_default.set_text_font(lv.font_montserrat_40)
    except AttributeError:
        style_main_scrn_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_main_scrn_ta_1_main_main_default.set_text_letter_space(2)
style_main_scrn_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_main_scrn_ta_1_main_main_default.set_pad_left(4)
style_main_scrn_ta_1_main_main_default.set_pad_right(4)
style_main_scrn_ta_1_main_main_default.set_pad_top(4)
style_main_scrn_ta_1_main_main_default.set_pad_bottom(4)

# add style for Main_scrn_ta_1
Main_scrn_ta_1.add_style(style_main_scrn_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_main_scrn_ta_1_main_scrollbar_default
style_main_scrn_ta_1_main_scrollbar_default = lv.style_t()
style_main_scrn_ta_1_main_scrollbar_default.init()
style_main_scrn_ta_1_main_scrollbar_default.set_radius(0)
style_main_scrn_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_main_scrn_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Main_scrn_ta_1
Main_scrn_ta_1.add_style(style_main_scrn_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Main_scrn_btn_1
Main_scrn_btn_1 = lv.btn(Main_scrn)
Main_scrn_btn_1.set_pos(int(497),int(547))
Main_scrn_btn_1.set_size(242,72)
Main_scrn_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Main_scrn_btn_1_label = lv.label(Main_scrn_btn_1)
Main_scrn_btn_1_label.set_text("START EXPLORING ")
Main_scrn_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Main_scrn_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_main_scrn_btn_1_main_main_default
style_main_scrn_btn_1_main_main_default = lv.style_t()
style_main_scrn_btn_1_main_main_default.init()
style_main_scrn_btn_1_main_main_default.set_radius(9)
style_main_scrn_btn_1_main_main_default.set_bg_color(lv.color_make(0x41,0x60,0x6e))
style_main_scrn_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_main_scrn_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_main_scrn_btn_1_main_main_default.set_bg_opa(255)
style_main_scrn_btn_1_main_main_default.set_shadow_width(1)
style_main_scrn_btn_1_main_main_default.set_shadow_color(lv.color_make(0x06,0x15,0x21))
style_main_scrn_btn_1_main_main_default.set_shadow_opa(255)
style_main_scrn_btn_1_main_main_default.set_shadow_spread(0)
style_main_scrn_btn_1_main_main_default.set_shadow_ofs_x(3)
style_main_scrn_btn_1_main_main_default.set_shadow_ofs_y(6)
style_main_scrn_btn_1_main_main_default.set_border_color(lv.color_make(0x0c,0x18,0x21))
style_main_scrn_btn_1_main_main_default.set_border_width(6)
style_main_scrn_btn_1_main_main_default.set_border_opa(255)
style_main_scrn_btn_1_main_main_default.set_text_color(lv.color_make(0xd6,0xe8,0xac))
try:
    style_main_scrn_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_26)
except AttributeError:
    try:
        style_main_scrn_btn_1_main_main_default.set_text_font(lv.font_montserrat_26)
    except AttributeError:
        style_main_scrn_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_main_scrn_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Main_scrn_btn_1
Main_scrn_btn_1.add_style(style_main_scrn_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn
Help_scrn = lv.obj()
Help_scrn.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_help_scrn_main_main_default
style_help_scrn_main_main_default = lv.style_t()
style_help_scrn_main_main_default.init()
style_help_scrn_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_help_scrn_main_main_default.set_bg_opa(0)

# add style for Help_scrn
Help_scrn.add_style(style_help_scrn_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_cont_1
Help_scrn_cont_1 = lv.obj(Help_scrn)
Help_scrn_cont_1.set_pos(int(0),int(0))
Help_scrn_cont_1.set_size(1280,720)
Help_scrn_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Help_scrn_img_1
Help_scrn_img_1 = lv.img(Help_scrn_cont_1)
Help_scrn_img_1.set_pos(int(0),int(0))
Help_scrn_img_1.set_size(1280,720)
Help_scrn_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Help_scrn_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Help_scrn_img_1_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_1_img_data
})

Help_scrn_img_1.set_src(Help_scrn_img_1_img)
Help_scrn_img_1.set_pivot(50,50)
Help_scrn_img_1.set_angle(0)
# create style style_help_scrn_img_1_main_main_default
style_help_scrn_img_1_main_main_default = lv.style_t()
style_help_scrn_img_1_main_main_default.init()
style_help_scrn_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_help_scrn_img_1_main_main_default.set_img_recolor_opa(48)
style_help_scrn_img_1_main_main_default.set_img_opa(177)

# add style for Help_scrn_img_1
Help_scrn_img_1.add_style(style_help_scrn_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_label_1
Help_scrn_label_1 = lv.label(Help_scrn_cont_1)
Help_scrn_label_1.set_pos(int(315),int(8))
Help_scrn_label_1.set_size(357,704)
Help_scrn_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_label_1.set_text("Sign commands:\n\nNEXT   -------->\n\n\nSTART  ------->\n\n\nBACK   -------->\n\n\nONE   ---------->\n\n\nTWO   --------->\n\n\nTHREE   ------->\n\n\nFOUR   ------->\n\n\nFIVE   -------->\n")
Help_scrn_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_help_scrn_label_1_main_main_default
style_help_scrn_label_1_main_main_default = lv.style_t()
style_help_scrn_label_1_main_main_default.init()
style_help_scrn_label_1_main_main_default.set_radius(0)
style_help_scrn_label_1_main_main_default.set_bg_color(lv.color_make(0xC3,0x4B,0xB5))
style_help_scrn_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x01,0x01))
style_help_scrn_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_help_scrn_label_1_main_main_default.set_bg_opa(255)
style_help_scrn_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_help_scrn_label_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_help_scrn_label_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_help_scrn_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_help_scrn_label_1_main_main_default.set_text_letter_space(2)
style_help_scrn_label_1_main_main_default.set_text_line_space(0)
style_help_scrn_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_help_scrn_label_1_main_main_default.set_pad_left(0)
style_help_scrn_label_1_main_main_default.set_pad_right(0)
style_help_scrn_label_1_main_main_default.set_pad_top(8)
style_help_scrn_label_1_main_main_default.set_pad_bottom(0)

# add style for Help_scrn_label_1
Help_scrn_label_1.add_style(style_help_scrn_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_label_2
Help_scrn_label_2 = lv.label(Help_scrn_cont_1)
Help_scrn_label_2.set_pos(int(717),int(7))
Help_scrn_label_2.set_size(506,123)
Help_scrn_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_label_2.set_text("Say the Wake Word \"HEY NXP\" , To Start the Voice Recognition")
Help_scrn_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_help_scrn_label_2_main_main_default
style_help_scrn_label_2_main_main_default = lv.style_t()
style_help_scrn_label_2_main_main_default.init()
style_help_scrn_label_2_main_main_default.set_radius(0)
style_help_scrn_label_2_main_main_default.set_bg_color(lv.color_make(0xc3,0x4b,0xb5))
style_help_scrn_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x06,0x00,0x00))
style_help_scrn_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_help_scrn_label_2_main_main_default.set_bg_opa(255)
style_help_scrn_label_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_help_scrn_label_2_main_main_default.set_text_font(lv.font_Acme_Regular_34)
except AttributeError:
    try:
        style_help_scrn_label_2_main_main_default.set_text_font(lv.font_montserrat_34)
    except AttributeError:
        style_help_scrn_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_help_scrn_label_2_main_main_default.set_text_letter_space(3)
style_help_scrn_label_2_main_main_default.set_text_line_space(0)
style_help_scrn_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_help_scrn_label_2_main_main_default.set_pad_left(0)
style_help_scrn_label_2_main_main_default.set_pad_right(0)
style_help_scrn_label_2_main_main_default.set_pad_top(9)
style_help_scrn_label_2_main_main_default.set_pad_bottom(0)

# add style for Help_scrn_label_2
Help_scrn_label_2.add_style(style_help_scrn_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_label_3
Help_scrn_label_3 = lv.label(Help_scrn_cont_1)
Help_scrn_label_3.set_pos(int(835),int(139))
Help_scrn_label_3.set_size(321,574)
Help_scrn_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_label_3.set_text("Voice Commands:\n\nNEXT\n\nSTART\n\nBACK\n\nHISTORY\n\nDESCRIPTION\n\nDEPICTION\n\nINTERPRETATION\n\nSTYLE\n\n")
Help_scrn_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_help_scrn_label_3_main_main_default
style_help_scrn_label_3_main_main_default = lv.style_t()
style_help_scrn_label_3_main_main_default.init()
style_help_scrn_label_3_main_main_default.set_radius(0)
style_help_scrn_label_3_main_main_default.set_bg_color(lv.color_make(0xC3,0x4B,0xB5))
style_help_scrn_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x04,0x0d,0x16))
style_help_scrn_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_help_scrn_label_3_main_main_default.set_bg_opa(255)
style_help_scrn_label_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_help_scrn_label_3_main_main_default.set_text_font(lv.font_Acme_Regular_32)
except AttributeError:
    try:
        style_help_scrn_label_3_main_main_default.set_text_font(lv.font_montserrat_32)
    except AttributeError:
        style_help_scrn_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_help_scrn_label_3_main_main_default.set_text_letter_space(2)
style_help_scrn_label_3_main_main_default.set_text_line_space(0)
style_help_scrn_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_help_scrn_label_3_main_main_default.set_pad_left(0)
style_help_scrn_label_3_main_main_default.set_pad_right(0)
style_help_scrn_label_3_main_main_default.set_pad_top(8)
style_help_scrn_label_3_main_main_default.set_pad_bottom(0)

# add style for Help_scrn_label_3
Help_scrn_label_3.add_style(style_help_scrn_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_3
Help_scrn_img_3 = lv.img(Help_scrn_cont_1)
Help_scrn_img_3.set_pos(int(585),int(55))
Help_scrn_img_3.set_size(83,61)
Help_scrn_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-271570908.png','rb') as f:
        Help_scrn_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-271570908.png')
    sys.exit()

Help_scrn_img_3_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_3_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_3_img_data
})

Help_scrn_img_3.set_src(Help_scrn_img_3_img)
Help_scrn_img_3.set_pivot(50,50)
Help_scrn_img_3.set_angle(0)
# create style style_help_scrn_img_3_main_main_default
style_help_scrn_img_3_main_main_default = lv.style_t()
style_help_scrn_img_3_main_main_default.init()
style_help_scrn_img_3_main_main_default.set_img_recolor(lv.color_make(0xfd,0xfd,0xfd))
style_help_scrn_img_3_main_main_default.set_img_recolor_opa(255)
style_help_scrn_img_3_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_3
Help_scrn_img_3.add_style(style_help_scrn_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_4
Help_scrn_img_4 = lv.img(Help_scrn_cont_1)
Help_scrn_img_4.set_pos(int(577),int(136))
Help_scrn_img_4.set_size(83,61)
Help_scrn_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1877234618.png','rb') as f:
        Help_scrn_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1877234618.png')
    sys.exit()

Help_scrn_img_4_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_4_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_4_img_data
})

Help_scrn_img_4.set_src(Help_scrn_img_4_img)
Help_scrn_img_4.set_pivot(50,50)
Help_scrn_img_4.set_angle(0)
# create style style_help_scrn_img_4_main_main_default
style_help_scrn_img_4_main_main_default = lv.style_t()
style_help_scrn_img_4_main_main_default.init()
style_help_scrn_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_4_main_main_default.set_img_recolor_opa(225)
style_help_scrn_img_4_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_4
Help_scrn_img_4.add_style(style_help_scrn_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_5
Help_scrn_img_5 = lv.img(Help_scrn_cont_1)
Help_scrn_img_5.set_pos(int(580),int(226))
Help_scrn_img_5.set_size(83,61)
Help_scrn_img_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-422877238.png','rb') as f:
        Help_scrn_img_5_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-422877238.png')
    sys.exit()

Help_scrn_img_5_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_5_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_5_img_data
})

Help_scrn_img_5.set_src(Help_scrn_img_5_img)
Help_scrn_img_5.set_pivot(50,50)
Help_scrn_img_5.set_angle(0)
# create style style_help_scrn_img_5_main_main_default
style_help_scrn_img_5_main_main_default = lv.style_t()
style_help_scrn_img_5_main_main_default.init()
style_help_scrn_img_5_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_5_main_main_default.set_img_recolor_opa(223)
style_help_scrn_img_5_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_5
Help_scrn_img_5.add_style(style_help_scrn_img_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_6
Help_scrn_img_6 = lv.img(Help_scrn_cont_1)
Help_scrn_img_6.set_pos(int(575),int(310))
Help_scrn_img_6.set_size(83,61)
Help_scrn_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1655984033.png','rb') as f:
        Help_scrn_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1655984033.png')
    sys.exit()

Help_scrn_img_6_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_6_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_6_img_data
})

Help_scrn_img_6.set_src(Help_scrn_img_6_img)
Help_scrn_img_6.set_pivot(50,50)
Help_scrn_img_6.set_angle(0)
# create style style_help_scrn_img_6_main_main_default
style_help_scrn_img_6_main_main_default = lv.style_t()
style_help_scrn_img_6_main_main_default.init()
style_help_scrn_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_6_main_main_default.set_img_recolor_opa(247)
style_help_scrn_img_6_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_6
Help_scrn_img_6.add_style(style_help_scrn_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_7
Help_scrn_img_7 = lv.img(Help_scrn_cont_1)
Help_scrn_img_7.set_pos(int(578),int(397))
Help_scrn_img_7.set_size(83,61)
Help_scrn_img_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1143959161.png','rb') as f:
        Help_scrn_img_7_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1143959161.png')
    sys.exit()

Help_scrn_img_7_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_7_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_7_img_data
})

Help_scrn_img_7.set_src(Help_scrn_img_7_img)
Help_scrn_img_7.set_pivot(50,50)
Help_scrn_img_7.set_angle(0)
# create style style_help_scrn_img_7_main_main_default
style_help_scrn_img_7_main_main_default = lv.style_t()
style_help_scrn_img_7_main_main_default.init()
style_help_scrn_img_7_main_main_default.set_img_recolor(lv.color_make(0xfe,0xfe,0xfe))
style_help_scrn_img_7_main_main_default.set_img_recolor_opa(234)
style_help_scrn_img_7_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_7
Help_scrn_img_7.add_style(style_help_scrn_img_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_8
Help_scrn_img_8 = lv.img(Help_scrn_cont_1)
Help_scrn_img_8.set_pos(int(578),int(474))
Help_scrn_img_8.set_size(83,61)
Help_scrn_img_8.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_8.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1872002457.png','rb') as f:
        Help_scrn_img_8_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1872002457.png')
    sys.exit()

Help_scrn_img_8_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_8_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_8_img_data
})

Help_scrn_img_8.set_src(Help_scrn_img_8_img)
Help_scrn_img_8.set_pivot(50,50)
Help_scrn_img_8.set_angle(0)
# create style style_help_scrn_img_8_main_main_default
style_help_scrn_img_8_main_main_default = lv.style_t()
style_help_scrn_img_8_main_main_default.init()
style_help_scrn_img_8_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_8_main_main_default.set_img_recolor_opa(255)
style_help_scrn_img_8_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_8
Help_scrn_img_8.add_style(style_help_scrn_img_8_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_9
Help_scrn_img_9 = lv.img(Help_scrn_cont_1)
Help_scrn_img_9.set_pos(int(577),int(556))
Help_scrn_img_9.set_size(83,61)
Help_scrn_img_9.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_9.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1736048297.png','rb') as f:
        Help_scrn_img_9_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1736048297.png')
    sys.exit()

Help_scrn_img_9_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_9_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_9_img_data
})

Help_scrn_img_9.set_src(Help_scrn_img_9_img)
Help_scrn_img_9.set_pivot(50,50)
Help_scrn_img_9.set_angle(0)
# create style style_help_scrn_img_9_main_main_default
style_help_scrn_img_9_main_main_default = lv.style_t()
style_help_scrn_img_9_main_main_default.init()
style_help_scrn_img_9_main_main_default.set_img_recolor(lv.color_make(0xf3,0xf3,0xf3))
style_help_scrn_img_9_main_main_default.set_img_recolor_opa(239)
style_help_scrn_img_9_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_9
Help_scrn_img_9.add_style(style_help_scrn_img_9_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_img_10
Help_scrn_img_10 = lv.img(Help_scrn_cont_1)
Help_scrn_img_10.set_pos(int(574),int(636))
Help_scrn_img_10.set_size(83,61)
Help_scrn_img_10.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1945827613.png','rb') as f:
        Help_scrn_img_10_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1945827613.png')
    sys.exit()

Help_scrn_img_10_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_10_img_data),
  'header': {'always_zero': 0, 'w': 83, 'h': 61, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_10_img_data
})

Help_scrn_img_10.set_src(Help_scrn_img_10_img)
Help_scrn_img_10.set_pivot(50,50)
Help_scrn_img_10.set_angle(0)
# create style style_help_scrn_img_10_main_main_default
style_help_scrn_img_10_main_main_default = lv.style_t()
style_help_scrn_img_10_main_main_default.init()
style_help_scrn_img_10_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_10_main_main_default.set_img_recolor_opa(255)
style_help_scrn_img_10_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_10
Help_scrn_img_10.add_style(style_help_scrn_img_10_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_help_scrn_cont_1_main_main_default
style_help_scrn_cont_1_main_main_default = lv.style_t()
style_help_scrn_cont_1_main_main_default.init()
style_help_scrn_cont_1_main_main_default.set_radius(0)
style_help_scrn_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_help_scrn_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_help_scrn_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_help_scrn_cont_1_main_main_default.set_bg_opa(255)
style_help_scrn_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_help_scrn_cont_1_main_main_default.set_border_width(2)
style_help_scrn_cont_1_main_main_default.set_border_opa(255)
style_help_scrn_cont_1_main_main_default.set_pad_left(0)
style_help_scrn_cont_1_main_main_default.set_pad_right(0)
style_help_scrn_cont_1_main_main_default.set_pad_top(0)
style_help_scrn_cont_1_main_main_default.set_pad_bottom(0)

# add style for Help_scrn_cont_1
Help_scrn_cont_1.add_style(style_help_scrn_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_cont_2
Help_scrn_cont_2 = lv.obj(Help_scrn)
Help_scrn_cont_2.set_pos(int(18),int(14))
Help_scrn_cont_2.set_size(266,109)
Help_scrn_cont_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Help_scrn_img_2
Help_scrn_img_2 = lv.img(Help_scrn_cont_2)
Help_scrn_img_2.set_pos(int(139),int(4))
Help_scrn_img_2.set_size(100,100)
Help_scrn_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Help_scrn_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1565784948.png','rb') as f:
        Help_scrn_img_2_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1565784948.png')
    sys.exit()

Help_scrn_img_2_img = lv.img_dsc_t({
  'data_size': len(Help_scrn_img_2_img_data),
  'header': {'always_zero': 0, 'w': 100, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_img_2_img_data
})

Help_scrn_img_2.set_src(Help_scrn_img_2_img)
Help_scrn_img_2.set_pivot(50,50)
Help_scrn_img_2.set_angle(0)
# create style style_help_scrn_img_2_main_main_default
style_help_scrn_img_2_main_main_default = lv.style_t()
style_help_scrn_img_2_main_main_default.init()
style_help_scrn_img_2_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_help_scrn_img_2_main_main_default.set_img_recolor_opa(0)
style_help_scrn_img_2_main_main_default.set_img_opa(255)

# add style for Help_scrn_img_2
Help_scrn_img_2.add_style(style_help_scrn_img_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Help_scrn_imgbtn_1
Help_scrn_imgbtn_1 = lv.imgbtn(Help_scrn_cont_2)
Help_scrn_imgbtn_1.set_pos(int(8),int(-1))
Help_scrn_imgbtn_1.set_size(112,103)
Help_scrn_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1775748682.png','rb') as f:
        Help_scrn_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1775748682.png')
    sys.exit()

Help_scrn_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(Help_scrn_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 112, 'h': 103, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_imgbtn_1_imgReleased_data
})
Help_scrn_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, None, Help_scrn_imgbtn_1_imgReleased, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1775748682.png','rb') as f:
        Help_scrn_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp-1775748682.png')
    sys.exit()

Help_scrn_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(Help_scrn_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 112, 'h': 103, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Help_scrn_imgbtn_1_imgPressed_data
})
Help_scrn_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, None, Help_scrn_imgbtn_1_imgPressed, None)




Help_scrn_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
# create style style_help_scrn_imgbtn_1_main_main_default
style_help_scrn_imgbtn_1_main_main_default = lv.style_t()
style_help_scrn_imgbtn_1_main_main_default.init()
style_help_scrn_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_help_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_montserratMedium_12)
except AttributeError:
    try:
        style_help_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_help_scrn_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_help_scrn_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_help_scrn_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0x71,0x17,0x73))
style_help_scrn_imgbtn_1_main_main_default.set_img_recolor_opa(0)
style_help_scrn_imgbtn_1_main_main_default.set_img_opa(255)

# add style for Help_scrn_imgbtn_1
Help_scrn_imgbtn_1.add_style(style_help_scrn_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_help_scrn_imgbtn_1_main_main_pressed
style_help_scrn_imgbtn_1_main_main_pressed = lv.style_t()
style_help_scrn_imgbtn_1_main_main_pressed.init()
style_help_scrn_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_help_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserratMedium_12)
except AttributeError:
    try:
        style_help_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_help_scrn_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_help_scrn_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_help_scrn_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_help_scrn_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for Help_scrn_imgbtn_1
Help_scrn_imgbtn_1.add_style(style_help_scrn_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_help_scrn_imgbtn_1_main_main_checked
style_help_scrn_imgbtn_1_main_main_checked = lv.style_t()
style_help_scrn_imgbtn_1_main_main_checked.init()
style_help_scrn_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_help_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserratMedium_12)
except AttributeError:
    try:
        style_help_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_help_scrn_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_help_scrn_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_help_scrn_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_help_scrn_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for Help_scrn_imgbtn_1
Help_scrn_imgbtn_1.add_style(style_help_scrn_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

# create style style_help_scrn_cont_2_main_main_default
style_help_scrn_cont_2_main_main_default = lv.style_t()
style_help_scrn_cont_2_main_main_default.init()
style_help_scrn_cont_2_main_main_default.set_radius(0)
style_help_scrn_cont_2_main_main_default.set_bg_color(lv.color_make(0xC3,0x4B,0xB5))
style_help_scrn_cont_2_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_help_scrn_cont_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_help_scrn_cont_2_main_main_default.set_bg_opa(255)
style_help_scrn_cont_2_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_help_scrn_cont_2_main_main_default.set_border_width(2)
style_help_scrn_cont_2_main_main_default.set_border_opa(255)
style_help_scrn_cont_2_main_main_default.set_pad_left(0)
style_help_scrn_cont_2_main_main_default.set_pad_right(0)
style_help_scrn_cont_2_main_main_default.set_pad_top(0)
style_help_scrn_cont_2_main_main_default.set_pad_bottom(0)

# add style for Help_scrn_cont_2
Help_scrn_cont_2.add_style(style_help_scrn_cont_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01
Art_01 = lv.obj()
Art_01.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_01_main_main_default
style_art_01_main_main_default = lv.style_t()
style_art_01_main_main_default.init()
style_art_01_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_main_main_default.set_bg_opa(0)

# add style for Art_01
Art_01.add_style(style_art_01_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_cont_1
Art_01_cont_1 = lv.obj(Art_01)
Art_01_cont_1.set_pos(int(-1),int(0))
Art_01_cont_1.set_size(1280,720)
Art_01_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_img_1
Art_01_img_1 = lv.img(Art_01_cont_1)
Art_01_img_1.set_pos(int(0),int(0))
Art_01_img_1.set_size(1280,720)
Art_01_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Art_01_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Art_01_img_1_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_1_img_data
})

Art_01_img_1.set_src(Art_01_img_1_img)
Art_01_img_1.set_pivot(50,50)
Art_01_img_1.set_angle(0)
# create style style_art_01_img_1_main_main_default
style_art_01_img_1_main_main_default = lv.style_t()
style_art_01_img_1_main_main_default.init()
style_art_01_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_art_01_img_1_main_main_default.set_img_recolor_opa(53)
style_art_01_img_1_main_main_default.set_img_opa(186)

# add style for Art_01_img_1
Art_01_img_1.add_style(style_art_01_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_img_2
Art_01_img_2 = lv.img(Art_01_cont_1)
Art_01_img_2.set_pos(int(58),int(33))
Art_01_img_2.set_size(326,353)
Art_01_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp81459986.png','rb') as f:
        Art_01_img_2_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp81459986.png')
    sys.exit()

Art_01_img_2_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_2_img_data),
  'header': {'always_zero': 0, 'w': 326, 'h': 353, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_2_img_data
})

Art_01_img_2.set_src(Art_01_img_2_img)
Art_01_img_2.set_pivot(50,50)
Art_01_img_2.set_angle(0)
# create style style_art_01_img_2_main_main_default
style_art_01_img_2_main_main_default = lv.style_t()
style_art_01_img_2_main_main_default.init()
style_art_01_img_2_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_img_2_main_main_default.set_img_recolor_opa(0)
style_art_01_img_2_main_main_default.set_img_opa(255)

# add style for Art_01_img_2
Art_01_img_2.add_style(style_art_01_img_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_label_1
Art_01_label_1 = lv.label(Art_01_cont_1)
Art_01_label_1.set_pos(int(509),int(71))
Art_01_label_1.set_size(754,306)
Art_01_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_label_1.set_text("Nataraja also known as Adalvallan is a depiction of Shiva, one of the main deities in Hinduism, as the divine cosmic dancer. His dance is called the tandava. The pose and artwork are described in many Hindu texts such as the Tevaram and Thiruvasagam in Tamil and the Amshumadagama and Uttarakamika agama in Sanskrit and the Grantha texts. The dance murti is featured in all major Hindu temples of Shaivism, and is a well-known sculptural symbol in India and popularly used as a symbol of Indian culture, as one of the finest illustrations of Hindu art. This form is also referred to as Kuththan , Sabesan , and Ambalavanan  in various Tamil texts.\n\nThe sculpture is symbolic of Shiva as the lord of dance and dramatic arts, with its style and proportions made according to Hindu texts on arts. Tamil devotional texts such as the Tirumurai (The twelve books of Southern Shaivism) state that Nataraja is the form of Shiva in which he performs his functions of creation, destruction, preservation, and is also attributed with maya and the act of blessing his devotees. Thus, Nataraja is considered one of the highest forms of Shiva in Tamil Nadu, and the sculpture or the bronze idol of Nataraja is worshipped in almost all Shiva temples across Tamil Nadu. It typically shows Shiva dancing in one of the Natya Shastra poses, holding various symbols which vary with historic period and region, trampling upon a demon shown as a dwarf (Apasmara or Muyalaka[4]) who symbolizes spiritual ignorance.\n\nThe classical form of the depiction appears in a pillar of rock cut temple at Seeyamangalam – Avanibhajana Pallaveshwaram Temple constructed by a Pallava King Mahendravarman I in 6th century CE, which is known by Archeological Survey of India and Archeological Survey of Tamil Nadu as the oldest known Nataraja sculpture in India. The stone reliefs at the Ellora Caves and the Badami Caves, by around the 6th century, are also among the oldest Nataraja sculptures in India. Ancient Tamil songs during the Bhakti movement written by the four Shaivite saints of Sambandar, Appar, Manikkavacakar, and Sundarar, popularly known as \"Nalvar\" (The four) extol Nataraja and describes the Nataraja Temple, Chidambaram as the home of Nataraja as the main deity, dating Nataraja worship way before the 7th century CE. Around the 8th to 10th century, statues emerged in Tamil Nadu in its mature and best-known expression in Chola bronzes, of various heights typically less than four feet, some over. Nataraja reliefs have been found in many parts of South East Asia such as Angkor Wat and in Bali, Cambodia, and Central Asia.")
Art_01_label_1.set_long_mode(lv.label.LONG.SCROLL)
# create style style_art_01_label_1_main_main_default
style_art_01_label_1_main_main_default = lv.style_t()
style_art_01_label_1_main_main_default.init()
style_art_01_label_1_main_main_default.set_radius(0)
style_art_01_label_1_main_main_default.set_bg_color(lv.color_make(0x76,0x2d,0x6d))
style_art_01_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x0d,0x01,0x0c))
style_art_01_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_art_01_label_1_main_main_default.set_bg_opa(255)
style_art_01_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_label_1_main_main_default.set_text_font(lv.font_Abel_regular_25)
except AttributeError:
    try:
        style_art_01_label_1_main_main_default.set_text_font(lv.font_montserrat_25)
    except AttributeError:
        style_art_01_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_label_1_main_main_default.set_text_letter_space(2)
style_art_01_label_1_main_main_default.set_text_line_space(5)
style_art_01_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_art_01_label_1_main_main_default.set_pad_left(7)
style_art_01_label_1_main_main_default.set_pad_right(0)
style_art_01_label_1_main_main_default.set_pad_top(8)
style_art_01_label_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_label_1
Art_01_label_1.add_style(style_art_01_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_ta_1
Art_01_ta_1 = lv.textarea(Art_01_cont_1)
Art_01_ta_1.set_pos(int(640),int(15))
Art_01_ta_1.set_size(438,41)
Art_01_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_ta_1.set_text("ARTIFACT-01    :     NATARAJA")


# create style style_art_01_ta_1_main_main_default
style_art_01_ta_1_main_main_default = lv.style_t()
style_art_01_ta_1_main_main_default.init()
style_art_01_ta_1_main_main_default.set_radius(5)
style_art_01_ta_1_main_main_default.set_bg_color(lv.color_make(0xb8,0x82,0xab))
style_art_01_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x6b,0x37,0x86))
style_art_01_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_ta_1_main_main_default.set_bg_opa(255)
style_art_01_ta_1_main_main_default.set_shadow_width(2)
style_art_01_ta_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_ta_1_main_main_default.set_shadow_opa(255)
style_art_01_ta_1_main_main_default.set_shadow_spread(0)
style_art_01_ta_1_main_main_default.set_shadow_ofs_x(-5)
style_art_01_ta_1_main_main_default.set_shadow_ofs_y(-3)
style_art_01_ta_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_ta_1_main_main_default.set_border_width(3)
style_art_01_ta_1_main_main_default.set_border_opa(255)
style_art_01_ta_1_main_main_default.set_text_color(lv.color_make(0xfe,0xfe,0xfe))
try:
    style_art_01_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_29)
except AttributeError:
    try:
        style_art_01_ta_1_main_main_default.set_text_font(lv.font_montserrat_29)
    except AttributeError:
        style_art_01_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_ta_1_main_main_default.set_text_letter_space(2)
style_art_01_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_art_01_ta_1_main_main_default.set_pad_left(4)
style_art_01_ta_1_main_main_default.set_pad_right(4)
style_art_01_ta_1_main_main_default.set_pad_top(4)
style_art_01_ta_1_main_main_default.set_pad_bottom(4)

# add style for Art_01_ta_1
Art_01_ta_1.add_style(style_art_01_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_ta_1_main_scrollbar_default
style_art_01_ta_1_main_scrollbar_default = lv.style_t()
style_art_01_ta_1_main_scrollbar_default.init()
style_art_01_ta_1_main_scrollbar_default.set_radius(0)
style_art_01_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Art_01_ta_1
Art_01_ta_1.add_style(style_art_01_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Art_01_btn_1
Art_01_btn_1 = lv.btn(Art_01_cont_1)
Art_01_btn_1.set_pos(int(514),int(430))
Art_01_btn_1.set_size(335,73)
Art_01_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_btn_1_label = lv.label(Art_01_btn_1)
Art_01_btn_1_label.set_text("1. HISTORY")
Art_01_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_btn_1_main_main_default
style_art_01_btn_1_main_main_default = lv.style_t()
style_art_01_btn_1_main_main_default.init()
style_art_01_btn_1_main_main_default.set_radius(9)
style_art_01_btn_1_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_btn_1_main_main_default.set_bg_opa(255)
style_art_01_btn_1_main_main_default.set_shadow_width(3)
style_art_01_btn_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_1_main_main_default.set_shadow_opa(255)
style_art_01_btn_1_main_main_default.set_shadow_spread(3)
style_art_01_btn_1_main_main_default.set_shadow_ofs_x(4)
style_art_01_btn_1_main_main_default.set_shadow_ofs_y(4)
style_art_01_btn_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_1_main_main_default.set_border_width(5)
style_art_01_btn_1_main_main_default.set_border_opa(255)
style_art_01_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_btn_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_btn_1
Art_01_btn_1.add_style(style_art_01_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_img_3
Art_01_img_3 = lv.img(Art_01_cont_1)
Art_01_img_3.set_pos(int(519),int(436))
Art_01_img_3.set_size(62,60)
Art_01_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png','rb') as f:
        Art_01_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png')
    sys.exit()

Art_01_img_3_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_3_img_data),
  'header': {'always_zero': 0, 'w': 62, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_3_img_data
})

Art_01_img_3.set_src(Art_01_img_3_img)
Art_01_img_3.set_pivot(50,50)
Art_01_img_3.set_angle(0)
# create style style_art_01_img_3_main_main_default
style_art_01_img_3_main_main_default = lv.style_t()
style_art_01_img_3_main_main_default.init()
style_art_01_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_img_3_main_main_default.set_img_recolor_opa(255)
style_art_01_img_3_main_main_default.set_img_opa(255)

# add style for Art_01_img_3
Art_01_img_3.add_style(style_art_01_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_btn_2
Art_01_btn_2 = lv.btn(Art_01_cont_1)
Art_01_btn_2.set_pos(int(925),int(435))
Art_01_btn_2.set_size(335,73)
Art_01_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_btn_2_label = lv.label(Art_01_btn_2)
Art_01_btn_2_label.set_text("2. DECEPTION")
Art_01_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_btn_2_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_btn_2_main_main_default
style_art_01_btn_2_main_main_default = lv.style_t()
style_art_01_btn_2_main_main_default.init()
style_art_01_btn_2_main_main_default.set_radius(9)
style_art_01_btn_2_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_btn_2_main_main_default.set_bg_opa(255)
style_art_01_btn_2_main_main_default.set_shadow_width(3)
style_art_01_btn_2_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_2_main_main_default.set_shadow_opa(255)
style_art_01_btn_2_main_main_default.set_shadow_spread(3)
style_art_01_btn_2_main_main_default.set_shadow_ofs_x(4)
style_art_01_btn_2_main_main_default.set_shadow_ofs_y(4)
style_art_01_btn_2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_2_main_main_default.set_border_width(5)
style_art_01_btn_2_main_main_default.set_border_opa(255)
style_art_01_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_btn_2_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_btn_2_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_btn_2
Art_01_btn_2.add_style(style_art_01_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_img_4
Art_01_img_4 = lv.img(Art_01_cont_1)
Art_01_img_4.set_pos(int(922),int(439))
Art_01_img_4.set_size(72,68)
Art_01_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png','rb') as f:
        Art_01_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png')
    sys.exit()

Art_01_img_4_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_4_img_data),
  'header': {'always_zero': 0, 'w': 72, 'h': 68, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_4_img_data
})

Art_01_img_4.set_src(Art_01_img_4_img)
Art_01_img_4.set_pivot(50,50)
Art_01_img_4.set_angle(0)
# create style style_art_01_img_4_main_main_default
style_art_01_img_4_main_main_default = lv.style_t()
style_art_01_img_4_main_main_default.init()
style_art_01_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_img_4_main_main_default.set_img_recolor_opa(252)
style_art_01_img_4_main_main_default.set_img_opa(255)

# add style for Art_01_img_4
Art_01_img_4.add_style(style_art_01_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_btn_3
Art_01_btn_3 = lv.btn(Art_01_cont_1)
Art_01_btn_3.set_pos(int(514),int(554))
Art_01_btn_3.set_size(335,73)
Art_01_btn_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_btn_3_label = lv.label(Art_01_btn_3)
Art_01_btn_3_label.set_text("3. INTERCEPTION")
Art_01_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_btn_3_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_btn_3_main_main_default
style_art_01_btn_3_main_main_default = lv.style_t()
style_art_01_btn_3_main_main_default.init()
style_art_01_btn_3_main_main_default.set_radius(9)
style_art_01_btn_3_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_btn_3_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_btn_3_main_main_default.set_bg_opa(255)
style_art_01_btn_3_main_main_default.set_shadow_width(3)
style_art_01_btn_3_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_3_main_main_default.set_shadow_opa(255)
style_art_01_btn_3_main_main_default.set_shadow_spread(3)
style_art_01_btn_3_main_main_default.set_shadow_ofs_x(4)
style_art_01_btn_3_main_main_default.set_shadow_ofs_y(4)
style_art_01_btn_3_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_3_main_main_default.set_border_width(5)
style_art_01_btn_3_main_main_default.set_border_opa(255)
style_art_01_btn_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_btn_3_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_btn_3_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_btn_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_btn_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_btn_3
Art_01_btn_3.add_style(style_art_01_btn_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_img_5
Art_01_img_5 = lv.img(Art_01_cont_1)
Art_01_img_5.set_pos(int(510),int(563))
Art_01_img_5.set_size(79,60)
Art_01_img_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp155653055.png','rb') as f:
        Art_01_img_5_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp155653055.png')
    sys.exit()

Art_01_img_5_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_5_img_data),
  'header': {'always_zero': 0, 'w': 79, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_5_img_data
})

Art_01_img_5.set_src(Art_01_img_5_img)
Art_01_img_5.set_pivot(50,50)
Art_01_img_5.set_angle(0)
# create style style_art_01_img_5_main_main_default
style_art_01_img_5_main_main_default = lv.style_t()
style_art_01_img_5_main_main_default.init()
style_art_01_img_5_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_img_5_main_main_default.set_img_recolor_opa(254)
style_art_01_img_5_main_main_default.set_img_opa(255)

# add style for Art_01_img_5
Art_01_img_5.add_style(style_art_01_img_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_btn_4
Art_01_btn_4 = lv.btn(Art_01_cont_1)
Art_01_btn_4.set_pos(int(926),int(561))
Art_01_btn_4.set_size(335,73)
Art_01_btn_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_btn_4_label = lv.label(Art_01_btn_4)
Art_01_btn_4_label.set_text("    NEXT ART")
Art_01_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_btn_4_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_btn_4_main_main_default
style_art_01_btn_4_main_main_default = lv.style_t()
style_art_01_btn_4_main_main_default.init()
style_art_01_btn_4_main_main_default.set_radius(9)
style_art_01_btn_4_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_btn_4_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_btn_4_main_main_default.set_bg_opa(255)
style_art_01_btn_4_main_main_default.set_shadow_width(3)
style_art_01_btn_4_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_4_main_main_default.set_shadow_opa(255)
style_art_01_btn_4_main_main_default.set_shadow_spread(3)
style_art_01_btn_4_main_main_default.set_shadow_ofs_x(4)
style_art_01_btn_4_main_main_default.set_shadow_ofs_y(4)
style_art_01_btn_4_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_btn_4_main_main_default.set_border_width(5)
style_art_01_btn_4_main_main_default.set_border_opa(255)
style_art_01_btn_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_btn_4_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_btn_4_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_btn_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_btn_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_btn_4
Art_01_btn_4.add_style(style_art_01_btn_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_img_6
Art_01_img_6 = lv.img(Art_01_cont_1)
Art_01_img_6.set_pos(int(939),int(560))
Art_01_img_6.set_size(92,70)
Art_01_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png','rb') as f:
        Art_01_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png')
    sys.exit()

Art_01_img_6_img = lv.img_dsc_t({
  'data_size': len(Art_01_img_6_img_data),
  'header': {'always_zero': 0, 'w': 92, 'h': 70, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_img_6_img_data
})

Art_01_img_6.set_src(Art_01_img_6_img)
Art_01_img_6.set_pivot(50,50)
Art_01_img_6.set_angle(0)
# create style style_art_01_img_6_main_main_default
style_art_01_img_6_main_main_default = lv.style_t()
style_art_01_img_6_main_main_default.init()
style_art_01_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_img_6_main_main_default.set_img_recolor_opa(251)
style_art_01_img_6_main_main_default.set_img_opa(255)

# add style for Art_01_img_6
Art_01_img_6.add_style(style_art_01_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_video_1
Art_01_video_1.set_pos(int(28),int(433))
Art_01_video_1.set_size(422,263)
Art_01_video_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_01_cont_1_main_main_default
style_art_01_cont_1_main_main_default = lv.style_t()
style_art_01_cont_1_main_main_default.init()
style_art_01_cont_1_main_main_default.set_radius(0)
style_art_01_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_art_01_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_art_01_cont_1_main_main_default.set_bg_opa(255)
style_art_01_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_cont_1_main_main_default.set_border_width(2)
style_art_01_cont_1_main_main_default.set_border_opa(255)
style_art_01_cont_1_main_main_default.set_pad_left(0)
style_art_01_cont_1_main_main_default.set_pad_right(0)
style_art_01_cont_1_main_main_default.set_pad_top(0)
style_art_01_cont_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_cont_1
Art_01_cont_1.add_style(style_art_01_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist
Art_01_hist = lv.obj()
Art_01_hist.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_01_hist_main_main_default
style_art_01_hist_main_main_default = lv.style_t()
style_art_01_hist_main_main_default.init()
style_art_01_hist_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_main_main_default.set_bg_opa(0)

# add style for Art_01_hist
Art_01_hist.add_style(style_art_01_hist_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_cont_1
Art_01_hist_cont_1 = lv.obj(Art_01_hist)
Art_01_hist_cont_1.set_pos(int(-1),int(0))
Art_01_hist_cont_1.set_size(1280,720)
Art_01_hist_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_hist_img_1
Art_01_hist_img_1 = lv.img(Art_01_hist_cont_1)
Art_01_hist_img_1.set_pos(int(0),int(0))
Art_01_hist_img_1.set_size(1280,720)
Art_01_hist_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_hist_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Art_01_hist_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Art_01_hist_img_1_img = lv.img_dsc_t({
  'data_size': len(Art_01_hist_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_hist_img_1_img_data
})

Art_01_hist_img_1.set_src(Art_01_hist_img_1_img)
Art_01_hist_img_1.set_pivot(50,50)
Art_01_hist_img_1.set_angle(0)
# create style style_art_01_hist_img_1_main_main_default
style_art_01_hist_img_1_main_main_default = lv.style_t()
style_art_01_hist_img_1_main_main_default.init()
style_art_01_hist_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_art_01_hist_img_1_main_main_default.set_img_recolor_opa(53)
style_art_01_hist_img_1_main_main_default.set_img_opa(186)

# add style for Art_01_hist_img_1
Art_01_hist_img_1.add_style(style_art_01_hist_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_label_1
Art_01_hist_label_1 = lv.label(Art_01_hist_cont_1)
Art_01_hist_label_1.set_pos(int(508),int(70))
Art_01_hist_label_1.set_size(754,306)
Art_01_hist_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_hist_label_1.set_text("Stone reliefs depicting the classical form of Nataraja are found in numerous cave temples of India, such as at the Ellora Caves (Maharashtra), the Elephanta Caves, and the Badami Caves (Karnataka), by around the 6th century. One of the earliest known Nataraja artworks has been found in the archaeological site at Asanapat village in Odisha, which includes an inscription, and is dated to about the 6th century CE. The Asanapat inscription also mentions a Shiva temple in the Saivacaryas kingdom.\n\nAround the 10th century, it emerged in Tamil Nadu in its mature and best-known expression in Chola bronzes, of various heights typically less than four feet. Nataraja reliefs are found in historic settings in many parts of South East Asia such as Ankor Wat, and in Bali, Cambodia, and central Asia. The oldest free-standing stone sculptures of Nataraja were built by Chola queen Sembiyan Mahadevi. Nataraja gained special significance and became a symbol of royalty in Tamil Nadu. The dancing Shiva became a part of Chola era processions and religious festivals, a practice that continued thereafter.\n\nIn 2004, a 2 meter statue of the dancing Shiva was unveiled at CERN, the European Center for Research in Particle Physics in Geneva. The statue, symbolizing Shiva's cosmic dance of creation and destruction, was given to CERN by the Indian government to celebrate the research center's long association with India. A special plaque next to the Shiva statue explains the metaphor of Shiva's cosmic dance with quotations from physicist Fritjof Capra:")
Art_01_hist_label_1.set_long_mode(lv.label.LONG.SCROLL)
# create style style_art_01_hist_label_1_main_main_default
style_art_01_hist_label_1_main_main_default = lv.style_t()
style_art_01_hist_label_1_main_main_default.init()
style_art_01_hist_label_1_main_main_default.set_radius(0)
style_art_01_hist_label_1_main_main_default.set_bg_color(lv.color_make(0x76,0x2d,0x6d))
style_art_01_hist_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x0d,0x01,0x0c))
style_art_01_hist_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_art_01_hist_label_1_main_main_default.set_bg_opa(255)
style_art_01_hist_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_hist_label_1_main_main_default.set_text_font(lv.font_Abel_regular_25)
except AttributeError:
    try:
        style_art_01_hist_label_1_main_main_default.set_text_font(lv.font_montserrat_25)
    except AttributeError:
        style_art_01_hist_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_label_1_main_main_default.set_text_letter_space(2)
style_art_01_hist_label_1_main_main_default.set_text_line_space(5)
style_art_01_hist_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_art_01_hist_label_1_main_main_default.set_pad_left(7)
style_art_01_hist_label_1_main_main_default.set_pad_right(0)
style_art_01_hist_label_1_main_main_default.set_pad_top(8)
style_art_01_hist_label_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_hist_label_1
Art_01_hist_label_1.add_style(style_art_01_hist_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_ta_1
Art_01_hist_ta_1 = lv.textarea(Art_01_hist_cont_1)
Art_01_hist_ta_1.set_pos(int(640),int(15))
Art_01_hist_ta_1.set_size(438,41)
Art_01_hist_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_hist_ta_1.set_text("HISTORY - NATARAJA")


# create style style_art_01_hist_ta_1_main_main_default
style_art_01_hist_ta_1_main_main_default = lv.style_t()
style_art_01_hist_ta_1_main_main_default.init()
style_art_01_hist_ta_1_main_main_default.set_radius(5)
style_art_01_hist_ta_1_main_main_default.set_bg_color(lv.color_make(0xb8,0x82,0xab))
style_art_01_hist_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x6b,0x37,0x86))
style_art_01_hist_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_hist_ta_1_main_main_default.set_bg_opa(255)
style_art_01_hist_ta_1_main_main_default.set_shadow_width(2)
style_art_01_hist_ta_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_ta_1_main_main_default.set_shadow_opa(255)
style_art_01_hist_ta_1_main_main_default.set_shadow_spread(0)
style_art_01_hist_ta_1_main_main_default.set_shadow_ofs_x(-5)
style_art_01_hist_ta_1_main_main_default.set_shadow_ofs_y(-3)
style_art_01_hist_ta_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_ta_1_main_main_default.set_border_width(3)
style_art_01_hist_ta_1_main_main_default.set_border_opa(255)
style_art_01_hist_ta_1_main_main_default.set_text_color(lv.color_make(0xfe,0xfe,0xfe))
try:
    style_art_01_hist_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_29)
except AttributeError:
    try:
        style_art_01_hist_ta_1_main_main_default.set_text_font(lv.font_montserrat_29)
    except AttributeError:
        style_art_01_hist_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_ta_1_main_main_default.set_text_letter_space(2)
style_art_01_hist_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_art_01_hist_ta_1_main_main_default.set_pad_left(4)
style_art_01_hist_ta_1_main_main_default.set_pad_right(4)
style_art_01_hist_ta_1_main_main_default.set_pad_top(4)
style_art_01_hist_ta_1_main_main_default.set_pad_bottom(4)

# add style for Art_01_hist_ta_1
Art_01_hist_ta_1.add_style(style_art_01_hist_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_hist_ta_1_main_scrollbar_default
style_art_01_hist_ta_1_main_scrollbar_default = lv.style_t()
style_art_01_hist_ta_1_main_scrollbar_default.init()
style_art_01_hist_ta_1_main_scrollbar_default.set_radius(0)
style_art_01_hist_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_hist_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Art_01_hist_ta_1
Art_01_hist_ta_1.add_style(style_art_01_hist_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Art_01_hist_btn_1
Art_01_hist_btn_1 = lv.btn(Art_01_hist_cont_1)
Art_01_hist_btn_1.set_pos(int(514),int(430))
Art_01_hist_btn_1.set_size(335,73)
Art_01_hist_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_btn_1_label = lv.label(Art_01_hist_btn_1)
Art_01_hist_btn_1_label.set_text("BACK")
Art_01_hist_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_hist_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_hist_btn_1_main_main_default
style_art_01_hist_btn_1_main_main_default = lv.style_t()
style_art_01_hist_btn_1_main_main_default.init()
style_art_01_hist_btn_1_main_main_default.set_radius(9)
style_art_01_hist_btn_1_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_hist_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_hist_btn_1_main_main_default.set_bg_opa(255)
style_art_01_hist_btn_1_main_main_default.set_shadow_width(3)
style_art_01_hist_btn_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_1_main_main_default.set_shadow_opa(255)
style_art_01_hist_btn_1_main_main_default.set_shadow_spread(3)
style_art_01_hist_btn_1_main_main_default.set_shadow_ofs_x(4)
style_art_01_hist_btn_1_main_main_default.set_shadow_ofs_y(4)
style_art_01_hist_btn_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_1_main_main_default.set_border_width(5)
style_art_01_hist_btn_1_main_main_default.set_border_opa(255)
style_art_01_hist_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_hist_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_hist_btn_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_hist_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_hist_btn_1
Art_01_hist_btn_1.add_style(style_art_01_hist_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_btn_2
Art_01_hist_btn_2 = lv.btn(Art_01_hist_cont_1)
Art_01_hist_btn_2.set_pos(int(925),int(435))
Art_01_hist_btn_2.set_size(335,73)
Art_01_hist_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_btn_2_label = lv.label(Art_01_hist_btn_2)
Art_01_hist_btn_2_label.set_text("1. DECEPTION")
Art_01_hist_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_hist_btn_2_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_hist_btn_2_main_main_default
style_art_01_hist_btn_2_main_main_default = lv.style_t()
style_art_01_hist_btn_2_main_main_default.init()
style_art_01_hist_btn_2_main_main_default.set_radius(9)
style_art_01_hist_btn_2_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_hist_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_hist_btn_2_main_main_default.set_bg_opa(255)
style_art_01_hist_btn_2_main_main_default.set_shadow_width(3)
style_art_01_hist_btn_2_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_2_main_main_default.set_shadow_opa(255)
style_art_01_hist_btn_2_main_main_default.set_shadow_spread(3)
style_art_01_hist_btn_2_main_main_default.set_shadow_ofs_x(4)
style_art_01_hist_btn_2_main_main_default.set_shadow_ofs_y(4)
style_art_01_hist_btn_2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_2_main_main_default.set_border_width(5)
style_art_01_hist_btn_2_main_main_default.set_border_opa(255)
style_art_01_hist_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_hist_btn_2_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_hist_btn_2_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_hist_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_hist_btn_2
Art_01_hist_btn_2.add_style(style_art_01_hist_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_img_3
Art_01_hist_img_3 = lv.img(Art_01_hist_cont_1)
Art_01_hist_img_3.set_pos(int(926),int(440))
Art_01_hist_img_3.set_size(62,60)
Art_01_hist_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png','rb') as f:
        Art_01_hist_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png')
    sys.exit()

Art_01_hist_img_3_img = lv.img_dsc_t({
  'data_size': len(Art_01_hist_img_3_img_data),
  'header': {'always_zero': 0, 'w': 62, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_hist_img_3_img_data
})

Art_01_hist_img_3.set_src(Art_01_hist_img_3_img)
Art_01_hist_img_3.set_pivot(50,50)
Art_01_hist_img_3.set_angle(0)
# create style style_art_01_hist_img_3_main_main_default
style_art_01_hist_img_3_main_main_default = lv.style_t()
style_art_01_hist_img_3_main_main_default.init()
style_art_01_hist_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_img_3_main_main_default.set_img_recolor_opa(255)
style_art_01_hist_img_3_main_main_default.set_img_opa(255)

# add style for Art_01_hist_img_3
Art_01_hist_img_3.add_style(style_art_01_hist_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_btn_3
Art_01_hist_btn_3 = lv.btn(Art_01_hist_cont_1)
Art_01_hist_btn_3.set_pos(int(513),int(559))
Art_01_hist_btn_3.set_size(335,73)
Art_01_hist_btn_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_btn_3_label = lv.label(Art_01_hist_btn_3)
Art_01_hist_btn_3_label.set_text("     2. INTERPRETATION")
Art_01_hist_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_hist_btn_3_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_hist_btn_3_main_main_default
style_art_01_hist_btn_3_main_main_default = lv.style_t()
style_art_01_hist_btn_3_main_main_default.init()
style_art_01_hist_btn_3_main_main_default.set_radius(9)
style_art_01_hist_btn_3_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_hist_btn_3_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_hist_btn_3_main_main_default.set_bg_opa(255)
style_art_01_hist_btn_3_main_main_default.set_shadow_width(3)
style_art_01_hist_btn_3_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_3_main_main_default.set_shadow_opa(255)
style_art_01_hist_btn_3_main_main_default.set_shadow_spread(3)
style_art_01_hist_btn_3_main_main_default.set_shadow_ofs_x(4)
style_art_01_hist_btn_3_main_main_default.set_shadow_ofs_y(4)
style_art_01_hist_btn_3_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_3_main_main_default.set_border_width(5)
style_art_01_hist_btn_3_main_main_default.set_border_opa(255)
style_art_01_hist_btn_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_hist_btn_3_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_hist_btn_3_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_hist_btn_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_btn_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_hist_btn_3
Art_01_hist_btn_3.add_style(style_art_01_hist_btn_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_img_4
Art_01_hist_img_4 = lv.img(Art_01_hist_cont_1)
Art_01_hist_img_4.set_pos(int(509),int(563))
Art_01_hist_img_4.set_size(72,68)
Art_01_hist_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png','rb') as f:
        Art_01_hist_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png')
    sys.exit()

Art_01_hist_img_4_img = lv.img_dsc_t({
  'data_size': len(Art_01_hist_img_4_img_data),
  'header': {'always_zero': 0, 'w': 72, 'h': 68, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_hist_img_4_img_data
})

Art_01_hist_img_4.set_src(Art_01_hist_img_4_img)
Art_01_hist_img_4.set_pivot(50,50)
Art_01_hist_img_4.set_angle(0)
# create style style_art_01_hist_img_4_main_main_default
style_art_01_hist_img_4_main_main_default = lv.style_t()
style_art_01_hist_img_4_main_main_default.init()
style_art_01_hist_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_img_4_main_main_default.set_img_recolor_opa(252)
style_art_01_hist_img_4_main_main_default.set_img_opa(255)

# add style for Art_01_hist_img_4
Art_01_hist_img_4.add_style(style_art_01_hist_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_btn_4
Art_01_hist_btn_4 = lv.btn(Art_01_hist_cont_1)
Art_01_hist_btn_4.set_pos(int(926),int(561))
Art_01_hist_btn_4.set_size(335,73)
Art_01_hist_btn_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_btn_4_label = lv.label(Art_01_hist_btn_4)
Art_01_hist_btn_4_label.set_text("      NEXT ART")
Art_01_hist_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_hist_btn_4_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_hist_btn_4_main_main_default
style_art_01_hist_btn_4_main_main_default = lv.style_t()
style_art_01_hist_btn_4_main_main_default.init()
style_art_01_hist_btn_4_main_main_default.set_radius(9)
style_art_01_hist_btn_4_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_hist_btn_4_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_hist_btn_4_main_main_default.set_bg_opa(255)
style_art_01_hist_btn_4_main_main_default.set_shadow_width(3)
style_art_01_hist_btn_4_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_4_main_main_default.set_shadow_opa(255)
style_art_01_hist_btn_4_main_main_default.set_shadow_spread(3)
style_art_01_hist_btn_4_main_main_default.set_shadow_ofs_x(4)
style_art_01_hist_btn_4_main_main_default.set_shadow_ofs_y(4)
style_art_01_hist_btn_4_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_hist_btn_4_main_main_default.set_border_width(5)
style_art_01_hist_btn_4_main_main_default.set_border_opa(255)
style_art_01_hist_btn_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_hist_btn_4_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_hist_btn_4_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_hist_btn_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_hist_btn_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_hist_btn_4
Art_01_hist_btn_4.add_style(style_art_01_hist_btn_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_img_6
Art_01_hist_img_6 = lv.img(Art_01_hist_cont_1)
Art_01_hist_img_6.set_pos(int(939),int(560))
Art_01_hist_img_6.set_size(92,70)
Art_01_hist_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png','rb') as f:
        Art_01_hist_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png')
    sys.exit()

Art_01_hist_img_6_img = lv.img_dsc_t({
  'data_size': len(Art_01_hist_img_6_img_data),
  'header': {'always_zero': 0, 'w': 92, 'h': 70, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_hist_img_6_img_data
})

Art_01_hist_img_6.set_src(Art_01_hist_img_6_img)
Art_01_hist_img_6.set_pivot(50,50)
Art_01_hist_img_6.set_angle(0)
# create style style_art_01_hist_img_6_main_main_default
style_art_01_hist_img_6_main_main_default = lv.style_t()
style_art_01_hist_img_6_main_main_default.init()
style_art_01_hist_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_img_6_main_main_default.set_img_recolor_opa(251)
style_art_01_hist_img_6_main_main_default.set_img_opa(255)

# add style for Art_01_hist_img_6
Art_01_hist_img_6.add_style(style_art_01_hist_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_hist_video_1
Art_01_hist_video_1.set_pos(int(20),int(85))
Art_01_hist_video_1.set_size(431,477)
Art_01_hist_video_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_hist_img_7
Art_01_hist_img_7 = lv.img(Art_01_hist_cont_1)
Art_01_hist_img_7.set_pos(int(523),int(433))
Art_01_hist_img_7.set_size(79,66)
Art_01_hist_img_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_hist_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png','rb') as f:
        Art_01_hist_img_7_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png')
    sys.exit()

Art_01_hist_img_7_img = lv.img_dsc_t({
  'data_size': len(Art_01_hist_img_7_img_data),
  'header': {'always_zero': 0, 'w': 79, 'h': 66, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_hist_img_7_img_data
})

Art_01_hist_img_7.set_src(Art_01_hist_img_7_img)
Art_01_hist_img_7.set_pivot(50,50)
Art_01_hist_img_7.set_angle(0)
# create style style_art_01_hist_img_7_main_main_default
style_art_01_hist_img_7_main_main_default = lv.style_t()
style_art_01_hist_img_7_main_main_default.init()
style_art_01_hist_img_7_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_img_7_main_main_default.set_img_recolor_opa(254)
style_art_01_hist_img_7_main_main_default.set_img_opa(255)

# add style for Art_01_hist_img_7
Art_01_hist_img_7.add_style(style_art_01_hist_img_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_hist_cont_1_main_main_default
style_art_01_hist_cont_1_main_main_default = lv.style_t()
style_art_01_hist_cont_1_main_main_default.init()
style_art_01_hist_cont_1_main_main_default.set_radius(0)
style_art_01_hist_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_art_01_hist_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_art_01_hist_cont_1_main_main_default.set_bg_opa(255)
style_art_01_hist_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_hist_cont_1_main_main_default.set_border_width(2)
style_art_01_hist_cont_1_main_main_default.set_border_opa(255)
style_art_01_hist_cont_1_main_main_default.set_pad_left(0)
style_art_01_hist_cont_1_main_main_default.set_pad_right(0)
style_art_01_hist_cont_1_main_main_default.set_pad_top(0)
style_art_01_hist_cont_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_hist_cont_1
Art_01_hist_cont_1.add_style(style_art_01_hist_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep
Art_01_decep = lv.obj()
Art_01_decep.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_01_decep_main_main_default
style_art_01_decep_main_main_default = lv.style_t()
style_art_01_decep_main_main_default.init()
style_art_01_decep_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_main_main_default.set_bg_opa(0)

# add style for Art_01_decep
Art_01_decep.add_style(style_art_01_decep_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_cont_1
Art_01_decep_cont_1 = lv.obj(Art_01_decep)
Art_01_decep_cont_1.set_pos(int(-1),int(0))
Art_01_decep_cont_1.set_size(1280,720)
Art_01_decep_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_decep_img_1
Art_01_decep_img_1 = lv.img(Art_01_decep_cont_1)
Art_01_decep_img_1.set_pos(int(0),int(0))
Art_01_decep_img_1.set_size(1280,720)
Art_01_decep_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_decep_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Art_01_decep_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Art_01_decep_img_1_img = lv.img_dsc_t({
  'data_size': len(Art_01_decep_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_decep_img_1_img_data
})

Art_01_decep_img_1.set_src(Art_01_decep_img_1_img)
Art_01_decep_img_1.set_pivot(50,50)
Art_01_decep_img_1.set_angle(0)
# create style style_art_01_decep_img_1_main_main_default
style_art_01_decep_img_1_main_main_default = lv.style_t()
style_art_01_decep_img_1_main_main_default.init()
style_art_01_decep_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_art_01_decep_img_1_main_main_default.set_img_recolor_opa(53)
style_art_01_decep_img_1_main_main_default.set_img_opa(186)

# add style for Art_01_decep_img_1
Art_01_decep_img_1.add_style(style_art_01_decep_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_label_1
Art_01_decep_label_1 = lv.label(Art_01_decep_cont_1)
Art_01_decep_label_1.set_pos(int(509),int(71))
Art_01_decep_label_1.set_size(754,306)
Art_01_decep_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_decep_label_1.set_text("The sculpture is symbolic of Shiva as the lord of dance and dramatic arts, with its style and proportions made according to Hindu texts on arts. The two most common forms of Shiva's dance are the Lasya (the gentle form of dance), associated with the creation of the world, and the Ananda Tandava (dance of bliss, the vigorous form of dance), associated with the destruction of weary worldview, weary perspectives and lifestyles. In essence, the Lasya and the Tandava are just two aspects of Shiva’s nature; for he destroys in order to create, tearing down to build again.\n\nIt typically shows Shiva dancing in one of the Natya Shastra poses, holding Agni (fire) in his left back hand, the front hand in gajahasta (elephant hand) or dandahasta (stick hand) mudra, the front right hand with a wrapped snake that is in abhaya (fear not) mudra while pointing to a Sutra text, and the back hand holding a musical instrument, usually a Udukai. His body, fingers, ankles, neck, face, head, ear lobes and dress are shown decorated with symbolic items, which vary with historic period and region. He is surrounded by a ring of flames, standing on a lotus pedestal, lifting his left leg (or in rare cases, the right leg) and balancing / trampling upon a demon shown as a dwarf (Apasmara or Muyalaka) who symbolizes spiritual ignorance. The dynamism of the energetic dance is depicted with the whirling hair which spread out in thin strands as a fan behind his head. The details in the Nataraja artwork have been variously interpreted by Indian scholars since the 12th century for its symbolic meaning and theological essence. Nataraja is a well known sculptural symbol in India and popularly used as a symbol of Indian culture, in particular as one of the finest illustrations of Hindu art.")
Art_01_decep_label_1.set_long_mode(lv.label.LONG.SCROLL)
# create style style_art_01_decep_label_1_main_main_default
style_art_01_decep_label_1_main_main_default = lv.style_t()
style_art_01_decep_label_1_main_main_default.init()
style_art_01_decep_label_1_main_main_default.set_radius(0)
style_art_01_decep_label_1_main_main_default.set_bg_color(lv.color_make(0x76,0x2d,0x6d))
style_art_01_decep_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x0d,0x01,0x0c))
style_art_01_decep_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_art_01_decep_label_1_main_main_default.set_bg_opa(255)
style_art_01_decep_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_decep_label_1_main_main_default.set_text_font(lv.font_Abel_regular_25)
except AttributeError:
    try:
        style_art_01_decep_label_1_main_main_default.set_text_font(lv.font_montserrat_25)
    except AttributeError:
        style_art_01_decep_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_label_1_main_main_default.set_text_letter_space(2)
style_art_01_decep_label_1_main_main_default.set_text_line_space(5)
style_art_01_decep_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_art_01_decep_label_1_main_main_default.set_pad_left(7)
style_art_01_decep_label_1_main_main_default.set_pad_right(0)
style_art_01_decep_label_1_main_main_default.set_pad_top(8)
style_art_01_decep_label_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_decep_label_1
Art_01_decep_label_1.add_style(style_art_01_decep_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_ta_1
Art_01_decep_ta_1 = lv.textarea(Art_01_decep_cont_1)
Art_01_decep_ta_1.set_pos(int(640),int(15))
Art_01_decep_ta_1.set_size(438,41)
Art_01_decep_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_decep_ta_1.set_text("DECEPTION - NATARAJA")


# create style style_art_01_decep_ta_1_main_main_default
style_art_01_decep_ta_1_main_main_default = lv.style_t()
style_art_01_decep_ta_1_main_main_default.init()
style_art_01_decep_ta_1_main_main_default.set_radius(5)
style_art_01_decep_ta_1_main_main_default.set_bg_color(lv.color_make(0xb8,0x82,0xab))
style_art_01_decep_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x6b,0x37,0x86))
style_art_01_decep_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_decep_ta_1_main_main_default.set_bg_opa(255)
style_art_01_decep_ta_1_main_main_default.set_shadow_width(2)
style_art_01_decep_ta_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_ta_1_main_main_default.set_shadow_opa(255)
style_art_01_decep_ta_1_main_main_default.set_shadow_spread(0)
style_art_01_decep_ta_1_main_main_default.set_shadow_ofs_x(-5)
style_art_01_decep_ta_1_main_main_default.set_shadow_ofs_y(-3)
style_art_01_decep_ta_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_ta_1_main_main_default.set_border_width(3)
style_art_01_decep_ta_1_main_main_default.set_border_opa(255)
style_art_01_decep_ta_1_main_main_default.set_text_color(lv.color_make(0xfe,0xfe,0xfe))
try:
    style_art_01_decep_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_29)
except AttributeError:
    try:
        style_art_01_decep_ta_1_main_main_default.set_text_font(lv.font_montserrat_29)
    except AttributeError:
        style_art_01_decep_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_ta_1_main_main_default.set_text_letter_space(2)
style_art_01_decep_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_art_01_decep_ta_1_main_main_default.set_pad_left(4)
style_art_01_decep_ta_1_main_main_default.set_pad_right(4)
style_art_01_decep_ta_1_main_main_default.set_pad_top(4)
style_art_01_decep_ta_1_main_main_default.set_pad_bottom(4)

# add style for Art_01_decep_ta_1
Art_01_decep_ta_1.add_style(style_art_01_decep_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_decep_ta_1_main_scrollbar_default
style_art_01_decep_ta_1_main_scrollbar_default = lv.style_t()
style_art_01_decep_ta_1_main_scrollbar_default.init()
style_art_01_decep_ta_1_main_scrollbar_default.set_radius(0)
style_art_01_decep_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_decep_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Art_01_decep_ta_1
Art_01_decep_ta_1.add_style(style_art_01_decep_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Art_01_decep_btn_1
Art_01_decep_btn_1 = lv.btn(Art_01_decep_cont_1)
Art_01_decep_btn_1.set_pos(int(514),int(430))
Art_01_decep_btn_1.set_size(335,73)
Art_01_decep_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_btn_1_label = lv.label(Art_01_decep_btn_1)
Art_01_decep_btn_1_label.set_text("BACK")
Art_01_decep_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_decep_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_decep_btn_1_main_main_default
style_art_01_decep_btn_1_main_main_default = lv.style_t()
style_art_01_decep_btn_1_main_main_default.init()
style_art_01_decep_btn_1_main_main_default.set_radius(9)
style_art_01_decep_btn_1_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_decep_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_decep_btn_1_main_main_default.set_bg_opa(255)
style_art_01_decep_btn_1_main_main_default.set_shadow_width(3)
style_art_01_decep_btn_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_1_main_main_default.set_shadow_opa(255)
style_art_01_decep_btn_1_main_main_default.set_shadow_spread(3)
style_art_01_decep_btn_1_main_main_default.set_shadow_ofs_x(4)
style_art_01_decep_btn_1_main_main_default.set_shadow_ofs_y(4)
style_art_01_decep_btn_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_1_main_main_default.set_border_width(5)
style_art_01_decep_btn_1_main_main_default.set_border_opa(255)
style_art_01_decep_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_decep_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_decep_btn_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_decep_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_decep_btn_1
Art_01_decep_btn_1.add_style(style_art_01_decep_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_btn_2
Art_01_decep_btn_2 = lv.btn(Art_01_decep_cont_1)
Art_01_decep_btn_2.set_pos(int(925),int(435))
Art_01_decep_btn_2.set_size(335,73)
Art_01_decep_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_btn_2_label = lv.label(Art_01_decep_btn_2)
Art_01_decep_btn_2_label.set_text("1. HISTORY")
Art_01_decep_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_decep_btn_2_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_decep_btn_2_main_main_default
style_art_01_decep_btn_2_main_main_default = lv.style_t()
style_art_01_decep_btn_2_main_main_default.init()
style_art_01_decep_btn_2_main_main_default.set_radius(9)
style_art_01_decep_btn_2_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_decep_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_decep_btn_2_main_main_default.set_bg_opa(255)
style_art_01_decep_btn_2_main_main_default.set_shadow_width(3)
style_art_01_decep_btn_2_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_2_main_main_default.set_shadow_opa(255)
style_art_01_decep_btn_2_main_main_default.set_shadow_spread(3)
style_art_01_decep_btn_2_main_main_default.set_shadow_ofs_x(4)
style_art_01_decep_btn_2_main_main_default.set_shadow_ofs_y(4)
style_art_01_decep_btn_2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_2_main_main_default.set_border_width(5)
style_art_01_decep_btn_2_main_main_default.set_border_opa(255)
style_art_01_decep_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_decep_btn_2_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_decep_btn_2_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_decep_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_decep_btn_2
Art_01_decep_btn_2.add_style(style_art_01_decep_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_img_3
Art_01_decep_img_3 = lv.img(Art_01_decep_cont_1)
Art_01_decep_img_3.set_pos(int(926),int(440))
Art_01_decep_img_3.set_size(62,60)
Art_01_decep_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png','rb') as f:
        Art_01_decep_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png')
    sys.exit()

Art_01_decep_img_3_img = lv.img_dsc_t({
  'data_size': len(Art_01_decep_img_3_img_data),
  'header': {'always_zero': 0, 'w': 62, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_decep_img_3_img_data
})

Art_01_decep_img_3.set_src(Art_01_decep_img_3_img)
Art_01_decep_img_3.set_pivot(50,50)
Art_01_decep_img_3.set_angle(0)
# create style style_art_01_decep_img_3_main_main_default
style_art_01_decep_img_3_main_main_default = lv.style_t()
style_art_01_decep_img_3_main_main_default.init()
style_art_01_decep_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_img_3_main_main_default.set_img_recolor_opa(255)
style_art_01_decep_img_3_main_main_default.set_img_opa(255)

# add style for Art_01_decep_img_3
Art_01_decep_img_3.add_style(style_art_01_decep_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_btn_3
Art_01_decep_btn_3 = lv.btn(Art_01_decep_cont_1)
Art_01_decep_btn_3.set_pos(int(513),int(559))
Art_01_decep_btn_3.set_size(335,73)
Art_01_decep_btn_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_btn_3_label = lv.label(Art_01_decep_btn_3)
Art_01_decep_btn_3_label.set_text("     2. INTERPRETATION")
Art_01_decep_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_decep_btn_3_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_decep_btn_3_main_main_default
style_art_01_decep_btn_3_main_main_default = lv.style_t()
style_art_01_decep_btn_3_main_main_default.init()
style_art_01_decep_btn_3_main_main_default.set_radius(9)
style_art_01_decep_btn_3_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_decep_btn_3_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_decep_btn_3_main_main_default.set_bg_opa(255)
style_art_01_decep_btn_3_main_main_default.set_shadow_width(3)
style_art_01_decep_btn_3_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_3_main_main_default.set_shadow_opa(255)
style_art_01_decep_btn_3_main_main_default.set_shadow_spread(3)
style_art_01_decep_btn_3_main_main_default.set_shadow_ofs_x(4)
style_art_01_decep_btn_3_main_main_default.set_shadow_ofs_y(4)
style_art_01_decep_btn_3_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_3_main_main_default.set_border_width(5)
style_art_01_decep_btn_3_main_main_default.set_border_opa(255)
style_art_01_decep_btn_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_decep_btn_3_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_decep_btn_3_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_decep_btn_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_btn_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_decep_btn_3
Art_01_decep_btn_3.add_style(style_art_01_decep_btn_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_img_4
Art_01_decep_img_4 = lv.img(Art_01_decep_cont_1)
Art_01_decep_img_4.set_pos(int(509),int(563))
Art_01_decep_img_4.set_size(72,68)
Art_01_decep_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png','rb') as f:
        Art_01_decep_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png')
    sys.exit()

Art_01_decep_img_4_img = lv.img_dsc_t({
  'data_size': len(Art_01_decep_img_4_img_data),
  'header': {'always_zero': 0, 'w': 72, 'h': 68, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_decep_img_4_img_data
})

Art_01_decep_img_4.set_src(Art_01_decep_img_4_img)
Art_01_decep_img_4.set_pivot(50,50)
Art_01_decep_img_4.set_angle(0)
# create style style_art_01_decep_img_4_main_main_default
style_art_01_decep_img_4_main_main_default = lv.style_t()
style_art_01_decep_img_4_main_main_default.init()
style_art_01_decep_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_img_4_main_main_default.set_img_recolor_opa(252)
style_art_01_decep_img_4_main_main_default.set_img_opa(255)

# add style for Art_01_decep_img_4
Art_01_decep_img_4.add_style(style_art_01_decep_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_btn_4
Art_01_decep_btn_4 = lv.btn(Art_01_decep_cont_1)
Art_01_decep_btn_4.set_pos(int(926),int(561))
Art_01_decep_btn_4.set_size(335,73)
Art_01_decep_btn_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_btn_4_label = lv.label(Art_01_decep_btn_4)
Art_01_decep_btn_4_label.set_text("      NEXT ART")
Art_01_decep_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_decep_btn_4_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_decep_btn_4_main_main_default
style_art_01_decep_btn_4_main_main_default = lv.style_t()
style_art_01_decep_btn_4_main_main_default.init()
style_art_01_decep_btn_4_main_main_default.set_radius(9)
style_art_01_decep_btn_4_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_decep_btn_4_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_decep_btn_4_main_main_default.set_bg_opa(255)
style_art_01_decep_btn_4_main_main_default.set_shadow_width(3)
style_art_01_decep_btn_4_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_4_main_main_default.set_shadow_opa(255)
style_art_01_decep_btn_4_main_main_default.set_shadow_spread(3)
style_art_01_decep_btn_4_main_main_default.set_shadow_ofs_x(4)
style_art_01_decep_btn_4_main_main_default.set_shadow_ofs_y(4)
style_art_01_decep_btn_4_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_decep_btn_4_main_main_default.set_border_width(5)
style_art_01_decep_btn_4_main_main_default.set_border_opa(255)
style_art_01_decep_btn_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_decep_btn_4_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_decep_btn_4_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_decep_btn_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_decep_btn_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_decep_btn_4
Art_01_decep_btn_4.add_style(style_art_01_decep_btn_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_img_6
Art_01_decep_img_6 = lv.img(Art_01_decep_cont_1)
Art_01_decep_img_6.set_pos(int(939),int(560))
Art_01_decep_img_6.set_size(92,70)
Art_01_decep_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png','rb') as f:
        Art_01_decep_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png')
    sys.exit()

Art_01_decep_img_6_img = lv.img_dsc_t({
  'data_size': len(Art_01_decep_img_6_img_data),
  'header': {'always_zero': 0, 'w': 92, 'h': 70, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_decep_img_6_img_data
})

Art_01_decep_img_6.set_src(Art_01_decep_img_6_img)
Art_01_decep_img_6.set_pivot(50,50)
Art_01_decep_img_6.set_angle(0)
# create style style_art_01_decep_img_6_main_main_default
style_art_01_decep_img_6_main_main_default = lv.style_t()
style_art_01_decep_img_6_main_main_default.init()
style_art_01_decep_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_img_6_main_main_default.set_img_recolor_opa(251)
style_art_01_decep_img_6_main_main_default.set_img_opa(255)

# add style for Art_01_decep_img_6
Art_01_decep_img_6.add_style(style_art_01_decep_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_decep_video_1
Art_01_decep_video_1.set_pos(int(20),int(85))
Art_01_decep_video_1.set_size(431,477)
Art_01_decep_video_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_decep_img_7
Art_01_decep_img_7 = lv.img(Art_01_decep_cont_1)
Art_01_decep_img_7.set_pos(int(523),int(433))
Art_01_decep_img_7.set_size(79,66)
Art_01_decep_img_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_decep_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png','rb') as f:
        Art_01_decep_img_7_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png')
    sys.exit()

Art_01_decep_img_7_img = lv.img_dsc_t({
  'data_size': len(Art_01_decep_img_7_img_data),
  'header': {'always_zero': 0, 'w': 79, 'h': 66, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_decep_img_7_img_data
})

Art_01_decep_img_7.set_src(Art_01_decep_img_7_img)
Art_01_decep_img_7.set_pivot(50,50)
Art_01_decep_img_7.set_angle(0)
# create style style_art_01_decep_img_7_main_main_default
style_art_01_decep_img_7_main_main_default = lv.style_t()
style_art_01_decep_img_7_main_main_default.init()
style_art_01_decep_img_7_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_img_7_main_main_default.set_img_recolor_opa(254)
style_art_01_decep_img_7_main_main_default.set_img_opa(255)

# add style for Art_01_decep_img_7
Art_01_decep_img_7.add_style(style_art_01_decep_img_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_decep_cont_1_main_main_default
style_art_01_decep_cont_1_main_main_default = lv.style_t()
style_art_01_decep_cont_1_main_main_default.init()
style_art_01_decep_cont_1_main_main_default.set_radius(0)
style_art_01_decep_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_art_01_decep_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_art_01_decep_cont_1_main_main_default.set_bg_opa(255)
style_art_01_decep_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_decep_cont_1_main_main_default.set_border_width(2)
style_art_01_decep_cont_1_main_main_default.set_border_opa(255)
style_art_01_decep_cont_1_main_main_default.set_pad_left(0)
style_art_01_decep_cont_1_main_main_default.set_pad_right(0)
style_art_01_decep_cont_1_main_main_default.set_pad_top(0)
style_art_01_decep_cont_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_decep_cont_1
Art_01_decep_cont_1.add_style(style_art_01_decep_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter
Art_01_inter = lv.obj()
Art_01_inter.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_01_inter_main_main_default
style_art_01_inter_main_main_default = lv.style_t()
style_art_01_inter_main_main_default.init()
style_art_01_inter_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_main_main_default.set_bg_opa(0)

# add style for Art_01_inter
Art_01_inter.add_style(style_art_01_inter_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_cont_1
Art_01_inter_cont_1 = lv.obj(Art_01_inter)
Art_01_inter_cont_1.set_pos(int(-1),int(0))
Art_01_inter_cont_1.set_size(1280,720)
Art_01_inter_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_inter_img_1
Art_01_inter_img_1 = lv.img(Art_01_inter_cont_1)
Art_01_inter_img_1.set_pos(int(0),int(0))
Art_01_inter_img_1.set_size(1280,720)
Art_01_inter_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_inter_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Art_01_inter_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Art_01_inter_img_1_img = lv.img_dsc_t({
  'data_size': len(Art_01_inter_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_inter_img_1_img_data
})

Art_01_inter_img_1.set_src(Art_01_inter_img_1_img)
Art_01_inter_img_1.set_pivot(50,50)
Art_01_inter_img_1.set_angle(0)
# create style style_art_01_inter_img_1_main_main_default
style_art_01_inter_img_1_main_main_default = lv.style_t()
style_art_01_inter_img_1_main_main_default.init()
style_art_01_inter_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_art_01_inter_img_1_main_main_default.set_img_recolor_opa(53)
style_art_01_inter_img_1_main_main_default.set_img_opa(186)

# add style for Art_01_inter_img_1
Art_01_inter_img_1.add_style(style_art_01_inter_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_label_1
Art_01_inter_label_1 = lv.label(Art_01_inter_cont_1)
Art_01_inter_label_1.set_pos(int(509),int(71))
Art_01_inter_label_1.set_size(754,306)
Art_01_inter_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_inter_label_1.set_text("Coomaraswamy summarizes the significance of Shiva's entire dance as an image of his rhythmic or musical play which is the source of all movement within the universe, represented by the arch surrounding Shiva. Secondly, the purpose of his dance is to release the souls of all men from illusion. And third, the place of the dance, Chidambaram, which is portrayed as the center of the universe, is actually within the heart.\n\nJames Lochtefeld states that Nataraja symbolizes \"the connection between religion and the arts\", and it represents Shiva as the lord of dance, encompassing all \"creation, destruction and all things in between\". The Nataraja iconography incorporates contrasting elements, a fearless celebration of the joys of dance while being surrounded by fire, untouched by forces of ignorance and evil, signifying a spirituality that transcends all duality. Furthermore, Carole and Pasquale note that the deity showcases the eternal cycle of life (Jiva) from death to rebirth, and how a human being should conquer spiritual ignorance and attain self-realization.\n\n")
Art_01_inter_label_1.set_long_mode(lv.label.LONG.SCROLL)
# create style style_art_01_inter_label_1_main_main_default
style_art_01_inter_label_1_main_main_default = lv.style_t()
style_art_01_inter_label_1_main_main_default.init()
style_art_01_inter_label_1_main_main_default.set_radius(0)
style_art_01_inter_label_1_main_main_default.set_bg_color(lv.color_make(0x76,0x2d,0x6d))
style_art_01_inter_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x0d,0x01,0x0c))
style_art_01_inter_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_art_01_inter_label_1_main_main_default.set_bg_opa(255)
style_art_01_inter_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_inter_label_1_main_main_default.set_text_font(lv.font_Abel_regular_25)
except AttributeError:
    try:
        style_art_01_inter_label_1_main_main_default.set_text_font(lv.font_montserrat_25)
    except AttributeError:
        style_art_01_inter_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_label_1_main_main_default.set_text_letter_space(2)
style_art_01_inter_label_1_main_main_default.set_text_line_space(5)
style_art_01_inter_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_art_01_inter_label_1_main_main_default.set_pad_left(7)
style_art_01_inter_label_1_main_main_default.set_pad_right(0)
style_art_01_inter_label_1_main_main_default.set_pad_top(8)
style_art_01_inter_label_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_inter_label_1
Art_01_inter_label_1.add_style(style_art_01_inter_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_ta_1
Art_01_inter_ta_1 = lv.textarea(Art_01_inter_cont_1)
Art_01_inter_ta_1.set_pos(int(640),int(15))
Art_01_inter_ta_1.set_size(438,41)
Art_01_inter_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_01_inter_ta_1.set_text("INTERPRETATION - NATARAJA")


# create style style_art_01_inter_ta_1_main_main_default
style_art_01_inter_ta_1_main_main_default = lv.style_t()
style_art_01_inter_ta_1_main_main_default.init()
style_art_01_inter_ta_1_main_main_default.set_radius(5)
style_art_01_inter_ta_1_main_main_default.set_bg_color(lv.color_make(0xb8,0x82,0xab))
style_art_01_inter_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x6b,0x37,0x86))
style_art_01_inter_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_inter_ta_1_main_main_default.set_bg_opa(255)
style_art_01_inter_ta_1_main_main_default.set_shadow_width(2)
style_art_01_inter_ta_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_ta_1_main_main_default.set_shadow_opa(255)
style_art_01_inter_ta_1_main_main_default.set_shadow_spread(0)
style_art_01_inter_ta_1_main_main_default.set_shadow_ofs_x(-5)
style_art_01_inter_ta_1_main_main_default.set_shadow_ofs_y(-3)
style_art_01_inter_ta_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_ta_1_main_main_default.set_border_width(3)
style_art_01_inter_ta_1_main_main_default.set_border_opa(255)
style_art_01_inter_ta_1_main_main_default.set_text_color(lv.color_make(0xfe,0xfe,0xfe))
try:
    style_art_01_inter_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_29)
except AttributeError:
    try:
        style_art_01_inter_ta_1_main_main_default.set_text_font(lv.font_montserrat_29)
    except AttributeError:
        style_art_01_inter_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_ta_1_main_main_default.set_text_letter_space(2)
style_art_01_inter_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_art_01_inter_ta_1_main_main_default.set_pad_left(4)
style_art_01_inter_ta_1_main_main_default.set_pad_right(4)
style_art_01_inter_ta_1_main_main_default.set_pad_top(4)
style_art_01_inter_ta_1_main_main_default.set_pad_bottom(4)

# add style for Art_01_inter_ta_1
Art_01_inter_ta_1.add_style(style_art_01_inter_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_inter_ta_1_main_scrollbar_default
style_art_01_inter_ta_1_main_scrollbar_default = lv.style_t()
style_art_01_inter_ta_1_main_scrollbar_default.init()
style_art_01_inter_ta_1_main_scrollbar_default.set_radius(0)
style_art_01_inter_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_inter_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Art_01_inter_ta_1
Art_01_inter_ta_1.add_style(style_art_01_inter_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Art_01_inter_btn_1
Art_01_inter_btn_1 = lv.btn(Art_01_inter_cont_1)
Art_01_inter_btn_1.set_pos(int(514),int(430))
Art_01_inter_btn_1.set_size(335,73)
Art_01_inter_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_btn_1_label = lv.label(Art_01_inter_btn_1)
Art_01_inter_btn_1_label.set_text("BACK")
Art_01_inter_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_inter_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_inter_btn_1_main_main_default
style_art_01_inter_btn_1_main_main_default = lv.style_t()
style_art_01_inter_btn_1_main_main_default.init()
style_art_01_inter_btn_1_main_main_default.set_radius(9)
style_art_01_inter_btn_1_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_inter_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_inter_btn_1_main_main_default.set_bg_opa(255)
style_art_01_inter_btn_1_main_main_default.set_shadow_width(3)
style_art_01_inter_btn_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_1_main_main_default.set_shadow_opa(255)
style_art_01_inter_btn_1_main_main_default.set_shadow_spread(3)
style_art_01_inter_btn_1_main_main_default.set_shadow_ofs_x(4)
style_art_01_inter_btn_1_main_main_default.set_shadow_ofs_y(4)
style_art_01_inter_btn_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_1_main_main_default.set_border_width(5)
style_art_01_inter_btn_1_main_main_default.set_border_opa(255)
style_art_01_inter_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_inter_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_inter_btn_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_inter_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_inter_btn_1
Art_01_inter_btn_1.add_style(style_art_01_inter_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_btn_2
Art_01_inter_btn_2 = lv.btn(Art_01_inter_cont_1)
Art_01_inter_btn_2.set_pos(int(925),int(435))
Art_01_inter_btn_2.set_size(335,73)
Art_01_inter_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_btn_2_label = lv.label(Art_01_inter_btn_2)
Art_01_inter_btn_2_label.set_text("1. HISTORY")
Art_01_inter_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_inter_btn_2_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_inter_btn_2_main_main_default
style_art_01_inter_btn_2_main_main_default = lv.style_t()
style_art_01_inter_btn_2_main_main_default.init()
style_art_01_inter_btn_2_main_main_default.set_radius(9)
style_art_01_inter_btn_2_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_inter_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_inter_btn_2_main_main_default.set_bg_opa(255)
style_art_01_inter_btn_2_main_main_default.set_shadow_width(3)
style_art_01_inter_btn_2_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_2_main_main_default.set_shadow_opa(255)
style_art_01_inter_btn_2_main_main_default.set_shadow_spread(3)
style_art_01_inter_btn_2_main_main_default.set_shadow_ofs_x(4)
style_art_01_inter_btn_2_main_main_default.set_shadow_ofs_y(4)
style_art_01_inter_btn_2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_2_main_main_default.set_border_width(5)
style_art_01_inter_btn_2_main_main_default.set_border_opa(255)
style_art_01_inter_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_inter_btn_2_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_inter_btn_2_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_inter_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_inter_btn_2
Art_01_inter_btn_2.add_style(style_art_01_inter_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_img_3
Art_01_inter_img_3 = lv.img(Art_01_inter_cont_1)
Art_01_inter_img_3.set_pos(int(926),int(440))
Art_01_inter_img_3.set_size(62,60)
Art_01_inter_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png','rb') as f:
        Art_01_inter_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png')
    sys.exit()

Art_01_inter_img_3_img = lv.img_dsc_t({
  'data_size': len(Art_01_inter_img_3_img_data),
  'header': {'always_zero': 0, 'w': 62, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_inter_img_3_img_data
})

Art_01_inter_img_3.set_src(Art_01_inter_img_3_img)
Art_01_inter_img_3.set_pivot(50,50)
Art_01_inter_img_3.set_angle(0)
# create style style_art_01_inter_img_3_main_main_default
style_art_01_inter_img_3_main_main_default = lv.style_t()
style_art_01_inter_img_3_main_main_default.init()
style_art_01_inter_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_img_3_main_main_default.set_img_recolor_opa(255)
style_art_01_inter_img_3_main_main_default.set_img_opa(255)

# add style for Art_01_inter_img_3
Art_01_inter_img_3.add_style(style_art_01_inter_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_btn_3
Art_01_inter_btn_3 = lv.btn(Art_01_inter_cont_1)
Art_01_inter_btn_3.set_pos(int(513),int(559))
Art_01_inter_btn_3.set_size(335,73)
Art_01_inter_btn_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_btn_3_label = lv.label(Art_01_inter_btn_3)
Art_01_inter_btn_3_label.set_text("2. DECEPTION")
Art_01_inter_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_inter_btn_3_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_inter_btn_3_main_main_default
style_art_01_inter_btn_3_main_main_default = lv.style_t()
style_art_01_inter_btn_3_main_main_default.init()
style_art_01_inter_btn_3_main_main_default.set_radius(9)
style_art_01_inter_btn_3_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_inter_btn_3_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_inter_btn_3_main_main_default.set_bg_opa(255)
style_art_01_inter_btn_3_main_main_default.set_shadow_width(3)
style_art_01_inter_btn_3_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_3_main_main_default.set_shadow_opa(255)
style_art_01_inter_btn_3_main_main_default.set_shadow_spread(3)
style_art_01_inter_btn_3_main_main_default.set_shadow_ofs_x(4)
style_art_01_inter_btn_3_main_main_default.set_shadow_ofs_y(4)
style_art_01_inter_btn_3_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_3_main_main_default.set_border_width(5)
style_art_01_inter_btn_3_main_main_default.set_border_opa(255)
style_art_01_inter_btn_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_inter_btn_3_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_inter_btn_3_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_inter_btn_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_btn_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_inter_btn_3
Art_01_inter_btn_3.add_style(style_art_01_inter_btn_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_img_4
Art_01_inter_img_4 = lv.img(Art_01_inter_cont_1)
Art_01_inter_img_4.set_pos(int(509),int(563))
Art_01_inter_img_4.set_size(72,68)
Art_01_inter_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png','rb') as f:
        Art_01_inter_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png')
    sys.exit()

Art_01_inter_img_4_img = lv.img_dsc_t({
  'data_size': len(Art_01_inter_img_4_img_data),
  'header': {'always_zero': 0, 'w': 72, 'h': 68, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_inter_img_4_img_data
})

Art_01_inter_img_4.set_src(Art_01_inter_img_4_img)
Art_01_inter_img_4.set_pivot(50,50)
Art_01_inter_img_4.set_angle(0)
# create style style_art_01_inter_img_4_main_main_default
style_art_01_inter_img_4_main_main_default = lv.style_t()
style_art_01_inter_img_4_main_main_default.init()
style_art_01_inter_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_img_4_main_main_default.set_img_recolor_opa(252)
style_art_01_inter_img_4_main_main_default.set_img_opa(255)

# add style for Art_01_inter_img_4
Art_01_inter_img_4.add_style(style_art_01_inter_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_btn_4
Art_01_inter_btn_4 = lv.btn(Art_01_inter_cont_1)
Art_01_inter_btn_4.set_pos(int(926),int(561))
Art_01_inter_btn_4.set_size(335,73)
Art_01_inter_btn_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_btn_4_label = lv.label(Art_01_inter_btn_4)
Art_01_inter_btn_4_label.set_text("      NEXT ART")
Art_01_inter_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_01_inter_btn_4_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_01_inter_btn_4_main_main_default
style_art_01_inter_btn_4_main_main_default = lv.style_t()
style_art_01_inter_btn_4_main_main_default.init()
style_art_01_inter_btn_4_main_main_default.set_radius(9)
style_art_01_inter_btn_4_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_01_inter_btn_4_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_01_inter_btn_4_main_main_default.set_bg_opa(255)
style_art_01_inter_btn_4_main_main_default.set_shadow_width(3)
style_art_01_inter_btn_4_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_4_main_main_default.set_shadow_opa(255)
style_art_01_inter_btn_4_main_main_default.set_shadow_spread(3)
style_art_01_inter_btn_4_main_main_default.set_shadow_ofs_x(4)
style_art_01_inter_btn_4_main_main_default.set_shadow_ofs_y(4)
style_art_01_inter_btn_4_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_01_inter_btn_4_main_main_default.set_border_width(5)
style_art_01_inter_btn_4_main_main_default.set_border_opa(255)
style_art_01_inter_btn_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_01_inter_btn_4_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_01_inter_btn_4_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_01_inter_btn_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_01_inter_btn_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_01_inter_btn_4
Art_01_inter_btn_4.add_style(style_art_01_inter_btn_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_img_6
Art_01_inter_img_6 = lv.img(Art_01_inter_cont_1)
Art_01_inter_img_6.set_pos(int(939),int(560))
Art_01_inter_img_6.set_size(92,70)
Art_01_inter_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png','rb') as f:
        Art_01_inter_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png')
    sys.exit()

Art_01_inter_img_6_img = lv.img_dsc_t({
  'data_size': len(Art_01_inter_img_6_img_data),
  'header': {'always_zero': 0, 'w': 92, 'h': 70, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_inter_img_6_img_data
})

Art_01_inter_img_6.set_src(Art_01_inter_img_6_img)
Art_01_inter_img_6.set_pivot(50,50)
Art_01_inter_img_6.set_angle(0)
# create style style_art_01_inter_img_6_main_main_default
style_art_01_inter_img_6_main_main_default = lv.style_t()
style_art_01_inter_img_6_main_main_default.init()
style_art_01_inter_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_img_6_main_main_default.set_img_recolor_opa(251)
style_art_01_inter_img_6_main_main_default.set_img_opa(255)

# add style for Art_01_inter_img_6
Art_01_inter_img_6.add_style(style_art_01_inter_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_01_inter_video_1
Art_01_inter_video_1.set_pos(int(20),int(85))
Art_01_inter_video_1.set_size(431,477)
Art_01_inter_video_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_01_inter_img_7
Art_01_inter_img_7 = lv.img(Art_01_inter_cont_1)
Art_01_inter_img_7.set_pos(int(523),int(433))
Art_01_inter_img_7.set_size(79,66)
Art_01_inter_img_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_01_inter_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png','rb') as f:
        Art_01_inter_img_7_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1685664246.png')
    sys.exit()

Art_01_inter_img_7_img = lv.img_dsc_t({
  'data_size': len(Art_01_inter_img_7_img_data),
  'header': {'always_zero': 0, 'w': 79, 'h': 66, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_01_inter_img_7_img_data
})

Art_01_inter_img_7.set_src(Art_01_inter_img_7_img)
Art_01_inter_img_7.set_pivot(50,50)
Art_01_inter_img_7.set_angle(0)
# create style style_art_01_inter_img_7_main_main_default
style_art_01_inter_img_7_main_main_default = lv.style_t()
style_art_01_inter_img_7_main_main_default.init()
style_art_01_inter_img_7_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_img_7_main_main_default.set_img_recolor_opa(254)
style_art_01_inter_img_7_main_main_default.set_img_opa(255)

# add style for Art_01_inter_img_7
Art_01_inter_img_7.add_style(style_art_01_inter_img_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_01_inter_cont_1_main_main_default
style_art_01_inter_cont_1_main_main_default = lv.style_t()
style_art_01_inter_cont_1_main_main_default.init()
style_art_01_inter_cont_1_main_main_default.set_radius(0)
style_art_01_inter_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_art_01_inter_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_art_01_inter_cont_1_main_main_default.set_bg_opa(255)
style_art_01_inter_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_art_01_inter_cont_1_main_main_default.set_border_width(2)
style_art_01_inter_cont_1_main_main_default.set_border_opa(255)
style_art_01_inter_cont_1_main_main_default.set_pad_left(0)
style_art_01_inter_cont_1_main_main_default.set_pad_right(0)
style_art_01_inter_cont_1_main_main_default.set_pad_top(0)
style_art_01_inter_cont_1_main_main_default.set_pad_bottom(0)

# add style for Art_01_inter_cont_1
Art_01_inter_cont_1.add_style(style_art_01_inter_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02
Art_02 = lv.obj()
Art_02.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_02_main_main_default
style_art_02_main_main_default = lv.style_t()
style_art_02_main_main_default.init()
style_art_02_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_02_main_main_default.set_bg_opa(0)

# add style for Art_02
Art_02.add_style(style_art_02_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_cont_1
Art_02_cont_1 = lv.obj(Art_02)
Art_02_cont_1.set_pos(int(-1),int(0))
Art_02_cont_1.set_size(1280,720)
Art_02_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create Art_02_img_1
Art_02_img_1 = lv.img(Art_02_cont_1)
Art_02_img_1.set_pos(int(0),int(0))
Art_02_img_1.set_size(1280,720)
Art_02_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_02_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png','rb') as f:
        Art_02_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp379480093.png')
    sys.exit()

Art_02_img_1_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_1_img_data),
  'header': {'always_zero': 0, 'w': 1280, 'h': 720, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_1_img_data
})

Art_02_img_1.set_src(Art_02_img_1_img)
Art_02_img_1.set_pivot(50,50)
Art_02_img_1.set_angle(0)
# create style style_art_02_img_1_main_main_default
style_art_02_img_1_main_main_default = lv.style_t()
style_art_02_img_1_main_main_default.init()
style_art_02_img_1_main_main_default.set_img_recolor(lv.color_make(0xFF,0x00,0xB2))
style_art_02_img_1_main_main_default.set_img_recolor_opa(53)
style_art_02_img_1_main_main_default.set_img_opa(186)

# add style for Art_02_img_1
Art_02_img_1.add_style(style_art_02_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_img_2
Art_02_img_2 = lv.img(Art_02_cont_1)
Art_02_img_2.set_pos(int(58),int(33))
Art_02_img_2.set_size(326,353)
Art_02_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1043074003.png','rb') as f:
        Art_02_img_2_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1043074003.png')
    sys.exit()

Art_02_img_2_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_2_img_data),
  'header': {'always_zero': 0, 'w': 326, 'h': 353, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_2_img_data
})

Art_02_img_2.set_src(Art_02_img_2_img)
Art_02_img_2.set_pivot(50,50)
Art_02_img_2.set_angle(0)
# create style style_art_02_img_2_main_main_default
style_art_02_img_2_main_main_default = lv.style_t()
style_art_02_img_2_main_main_default.init()
style_art_02_img_2_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_02_img_2_main_main_default.set_img_recolor_opa(0)
style_art_02_img_2_main_main_default.set_img_opa(255)

# add style for Art_02_img_2
Art_02_img_2.add_style(style_art_02_img_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_label_1
Art_02_label_1 = lv.label(Art_02_cont_1)
Art_02_label_1.set_pos(int(509),int(71))
Art_02_label_1.set_size(754,306)
Art_02_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_02_label_1.set_text("Dancing Girl is a prehistoric bronze sculpture made in lost-wax casting about c. 2300–1751 BC in the Indus Valley civilisation city of Mohenjo-daro (in modern-day Pakistan), which was one of the earliest cities. The statue is 10.5 centimetres (4.1 in) tall, and depicts a nude young woman or girl with stylized ornaments, standing in a confident, naturalistic pose. Dancing Girl is highly regarded as a work of art.\n\nThe statue was excavated by British archaeologist Ernest Mackay in the \"HR area\" of Mohenjo-daro in 1926. It is now in the National Museum, New Delhi, having been allocated to India at the Partition of India in 1947.")
Art_02_label_1.set_long_mode(lv.label.LONG.SCROLL)
# create style style_art_02_label_1_main_main_default
style_art_02_label_1_main_main_default = lv.style_t()
style_art_02_label_1_main_main_default.init()
style_art_02_label_1_main_main_default.set_radius(0)
style_art_02_label_1_main_main_default.set_bg_color(lv.color_make(0x76,0x2d,0x6d))
style_art_02_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x0d,0x01,0x0c))
style_art_02_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_art_02_label_1_main_main_default.set_bg_opa(255)
style_art_02_label_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_02_label_1_main_main_default.set_text_font(lv.font_Abel_regular_25)
except AttributeError:
    try:
        style_art_02_label_1_main_main_default.set_text_font(lv.font_montserrat_25)
    except AttributeError:
        style_art_02_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_label_1_main_main_default.set_text_letter_space(2)
style_art_02_label_1_main_main_default.set_text_line_space(5)
style_art_02_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.LEFT)
style_art_02_label_1_main_main_default.set_pad_left(7)
style_art_02_label_1_main_main_default.set_pad_right(0)
style_art_02_label_1_main_main_default.set_pad_top(8)
style_art_02_label_1_main_main_default.set_pad_bottom(0)

# add style for Art_02_label_1
Art_02_label_1.add_style(style_art_02_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_ta_1
Art_02_ta_1 = lv.textarea(Art_02_cont_1)
Art_02_ta_1.set_pos(int(640),int(15))
Art_02_ta_1.set_size(514,41)
Art_02_ta_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.ON)
Art_02_ta_1.set_text("ARTIFACT-02    :     DANCING GIRL")


# create style style_art_02_ta_1_main_main_default
style_art_02_ta_1_main_main_default = lv.style_t()
style_art_02_ta_1_main_main_default.init()
style_art_02_ta_1_main_main_default.set_radius(5)
style_art_02_ta_1_main_main_default.set_bg_color(lv.color_make(0xb8,0x82,0xab))
style_art_02_ta_1_main_main_default.set_bg_grad_color(lv.color_make(0x6b,0x37,0x86))
style_art_02_ta_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_02_ta_1_main_main_default.set_bg_opa(255)
style_art_02_ta_1_main_main_default.set_shadow_width(2)
style_art_02_ta_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_02_ta_1_main_main_default.set_shadow_opa(255)
style_art_02_ta_1_main_main_default.set_shadow_spread(0)
style_art_02_ta_1_main_main_default.set_shadow_ofs_x(-5)
style_art_02_ta_1_main_main_default.set_shadow_ofs_y(-3)
style_art_02_ta_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_02_ta_1_main_main_default.set_border_width(3)
style_art_02_ta_1_main_main_default.set_border_opa(255)
style_art_02_ta_1_main_main_default.set_text_color(lv.color_make(0xfe,0xfe,0xfe))
try:
    style_art_02_ta_1_main_main_default.set_text_font(lv.font_Acme_Regular_29)
except AttributeError:
    try:
        style_art_02_ta_1_main_main_default.set_text_font(lv.font_montserrat_29)
    except AttributeError:
        style_art_02_ta_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_ta_1_main_main_default.set_text_letter_space(2)
style_art_02_ta_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_art_02_ta_1_main_main_default.set_pad_left(4)
style_art_02_ta_1_main_main_default.set_pad_right(4)
style_art_02_ta_1_main_main_default.set_pad_top(4)
style_art_02_ta_1_main_main_default.set_pad_bottom(4)

# add style for Art_02_ta_1
Art_02_ta_1.add_style(style_art_02_ta_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_art_02_ta_1_main_scrollbar_default
style_art_02_ta_1_main_scrollbar_default = lv.style_t()
style_art_02_ta_1_main_scrollbar_default.init()
style_art_02_ta_1_main_scrollbar_default.set_radius(0)
style_art_02_ta_1_main_scrollbar_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_art_02_ta_1_main_scrollbar_default.set_bg_opa(255)

# add style for Art_02_ta_1
Art_02_ta_1.add_style(style_art_02_ta_1_main_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)


# create Art_02_btn_1
Art_02_btn_1 = lv.btn(Art_02_cont_1)
Art_02_btn_1.set_pos(int(514),int(430))
Art_02_btn_1.set_size(335,73)
Art_02_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_btn_1_label = lv.label(Art_02_btn_1)
Art_02_btn_1_label.set_text("1. HISTORY")
Art_02_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_02_btn_1_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_02_btn_1_main_main_default
style_art_02_btn_1_main_main_default = lv.style_t()
style_art_02_btn_1_main_main_default.init()
style_art_02_btn_1_main_main_default.set_radius(9)
style_art_02_btn_1_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_02_btn_1_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_02_btn_1_main_main_default.set_bg_opa(255)
style_art_02_btn_1_main_main_default.set_shadow_width(3)
style_art_02_btn_1_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_1_main_main_default.set_shadow_opa(255)
style_art_02_btn_1_main_main_default.set_shadow_spread(3)
style_art_02_btn_1_main_main_default.set_shadow_ofs_x(4)
style_art_02_btn_1_main_main_default.set_shadow_ofs_y(4)
style_art_02_btn_1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_1_main_main_default.set_border_width(5)
style_art_02_btn_1_main_main_default.set_border_opa(255)
style_art_02_btn_1_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_02_btn_1_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_02_btn_1_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_02_btn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_btn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_02_btn_1
Art_02_btn_1.add_style(style_art_02_btn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_img_3
Art_02_img_3 = lv.img(Art_02_cont_1)
Art_02_img_3.set_pos(int(519),int(436))
Art_02_img_3.set_size(62,60)
Art_02_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png','rb') as f:
        Art_02_img_3_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp1964794657.png')
    sys.exit()

Art_02_img_3_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_3_img_data),
  'header': {'always_zero': 0, 'w': 62, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_3_img_data
})

Art_02_img_3.set_src(Art_02_img_3_img)
Art_02_img_3.set_pivot(50,50)
Art_02_img_3.set_angle(0)
# create style style_art_02_img_3_main_main_default
style_art_02_img_3_main_main_default = lv.style_t()
style_art_02_img_3_main_main_default.init()
style_art_02_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_02_img_3_main_main_default.set_img_recolor_opa(255)
style_art_02_img_3_main_main_default.set_img_opa(255)

# add style for Art_02_img_3
Art_02_img_3.add_style(style_art_02_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_btn_2
Art_02_btn_2 = lv.btn(Art_02_cont_1)
Art_02_btn_2.set_pos(int(925),int(435))
Art_02_btn_2.set_size(335,73)
Art_02_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_btn_2_label = lv.label(Art_02_btn_2)
Art_02_btn_2_label.set_text("2. DESCRIPTION")
Art_02_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_02_btn_2_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_02_btn_2_main_main_default
style_art_02_btn_2_main_main_default = lv.style_t()
style_art_02_btn_2_main_main_default.init()
style_art_02_btn_2_main_main_default.set_radius(9)
style_art_02_btn_2_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_02_btn_2_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_02_btn_2_main_main_default.set_bg_opa(255)
style_art_02_btn_2_main_main_default.set_shadow_width(3)
style_art_02_btn_2_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_2_main_main_default.set_shadow_opa(255)
style_art_02_btn_2_main_main_default.set_shadow_spread(3)
style_art_02_btn_2_main_main_default.set_shadow_ofs_x(4)
style_art_02_btn_2_main_main_default.set_shadow_ofs_y(4)
style_art_02_btn_2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_2_main_main_default.set_border_width(5)
style_art_02_btn_2_main_main_default.set_border_opa(255)
style_art_02_btn_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_02_btn_2_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_02_btn_2_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_02_btn_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_btn_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_02_btn_2
Art_02_btn_2.add_style(style_art_02_btn_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_img_4
Art_02_img_4 = lv.img(Art_02_cont_1)
Art_02_img_4.set_pos(int(922),int(439))
Art_02_img_4.set_size(72,68)
Art_02_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png','rb') as f:
        Art_02_img_4_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp992570222.png')
    sys.exit()

Art_02_img_4_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_4_img_data),
  'header': {'always_zero': 0, 'w': 72, 'h': 68, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_4_img_data
})

Art_02_img_4.set_src(Art_02_img_4_img)
Art_02_img_4.set_pivot(50,50)
Art_02_img_4.set_angle(0)
# create style style_art_02_img_4_main_main_default
style_art_02_img_4_main_main_default = lv.style_t()
style_art_02_img_4_main_main_default.init()
style_art_02_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_02_img_4_main_main_default.set_img_recolor_opa(252)
style_art_02_img_4_main_main_default.set_img_opa(255)

# add style for Art_02_img_4
Art_02_img_4.add_style(style_art_02_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_btn_3
Art_02_btn_3 = lv.btn(Art_02_cont_1)
Art_02_btn_3.set_pos(int(514),int(554))
Art_02_btn_3.set_size(335,73)
Art_02_btn_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_btn_3_label = lv.label(Art_02_btn_3)
Art_02_btn_3_label.set_text("3. INTERCEPTION")
Art_02_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_02_btn_3_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_02_btn_3_main_main_default
style_art_02_btn_3_main_main_default = lv.style_t()
style_art_02_btn_3_main_main_default.init()
style_art_02_btn_3_main_main_default.set_radius(9)
style_art_02_btn_3_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_02_btn_3_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_02_btn_3_main_main_default.set_bg_opa(255)
style_art_02_btn_3_main_main_default.set_shadow_width(3)
style_art_02_btn_3_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_3_main_main_default.set_shadow_opa(255)
style_art_02_btn_3_main_main_default.set_shadow_spread(3)
style_art_02_btn_3_main_main_default.set_shadow_ofs_x(4)
style_art_02_btn_3_main_main_default.set_shadow_ofs_y(4)
style_art_02_btn_3_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_3_main_main_default.set_border_width(5)
style_art_02_btn_3_main_main_default.set_border_opa(255)
style_art_02_btn_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_02_btn_3_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_02_btn_3_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_02_btn_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_btn_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_02_btn_3
Art_02_btn_3.add_style(style_art_02_btn_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_img_5
Art_02_img_5 = lv.img(Art_02_cont_1)
Art_02_img_5.set_pos(int(510),int(563))
Art_02_img_5.set_size(79,60)
Art_02_img_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp155653055.png','rb') as f:
        Art_02_img_5_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp155653055.png')
    sys.exit()

Art_02_img_5_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_5_img_data),
  'header': {'always_zero': 0, 'w': 79, 'h': 60, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_5_img_data
})

Art_02_img_5.set_src(Art_02_img_5_img)
Art_02_img_5.set_pivot(50,50)
Art_02_img_5.set_angle(0)
# create style style_art_02_img_5_main_main_default
style_art_02_img_5_main_main_default = lv.style_t()
style_art_02_img_5_main_main_default.init()
style_art_02_img_5_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_02_img_5_main_main_default.set_img_recolor_opa(254)
style_art_02_img_5_main_main_default.set_img_opa(255)

# add style for Art_02_img_5
Art_02_img_5.add_style(style_art_02_img_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_btn_4
Art_02_btn_4 = lv.btn(Art_02_cont_1)
Art_02_btn_4.set_pos(int(926),int(561))
Art_02_btn_4.set_size(335,73)
Art_02_btn_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_btn_4_label = lv.label(Art_02_btn_4)
Art_02_btn_4_label.set_text("    NEXT ART")
Art_02_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
Art_02_btn_4_label.align(lv.ALIGN.CENTER,0,0)
# create style style_art_02_btn_4_main_main_default
style_art_02_btn_4_main_main_default = lv.style_t()
style_art_02_btn_4_main_main_default.init()
style_art_02_btn_4_main_main_default.set_radius(9)
style_art_02_btn_4_main_main_default.set_bg_color(lv.color_make(0x79,0x1e,0x6e))
style_art_02_btn_4_main_main_default.set_bg_grad_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_art_02_btn_4_main_main_default.set_bg_opa(255)
style_art_02_btn_4_main_main_default.set_shadow_width(3)
style_art_02_btn_4_main_main_default.set_shadow_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_4_main_main_default.set_shadow_opa(255)
style_art_02_btn_4_main_main_default.set_shadow_spread(3)
style_art_02_btn_4_main_main_default.set_shadow_ofs_x(4)
style_art_02_btn_4_main_main_default.set_shadow_ofs_y(4)
style_art_02_btn_4_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_art_02_btn_4_main_main_default.set_border_width(5)
style_art_02_btn_4_main_main_default.set_border_opa(255)
style_art_02_btn_4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_art_02_btn_4_main_main_default.set_text_font(lv.font_Acme_Regular_28)
except AttributeError:
    try:
        style_art_02_btn_4_main_main_default.set_text_font(lv.font_montserrat_28)
    except AttributeError:
        style_art_02_btn_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_art_02_btn_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)

# add style for Art_02_btn_4
Art_02_btn_4.add_style(style_art_02_btn_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_img_6
Art_02_img_6 = lv.img(Art_02_cont_1)
Art_02_img_6.set_pos(int(939),int(560))
Art_02_img_6.set_size(92,70)
Art_02_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
Art_02_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png','rb') as f:
        Art_02_img_6_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\Museum_Guide_bot\\generated\\mPythonImages\\mp2108661984.png')
    sys.exit()

Art_02_img_6_img = lv.img_dsc_t({
  'data_size': len(Art_02_img_6_img_data),
  'header': {'always_zero': 0, 'w': 92, 'h': 70, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': Art_02_img_6_img_data
})

Art_02_img_6.set_src(Art_02_img_6_img)
Art_02_img_6.set_pivot(50,50)
Art_02_img_6.set_angle(0)
# create style style_art_02_img_6_main_main_default
style_art_02_img_6_main_main_default = lv.style_t()
style_art_02_img_6_main_main_default.init()
style_art_02_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_art_02_img_6_main_main_default.set_img_recolor_opa(251)
style_art_02_img_6_main_main_default.set_img_opa(255)

# add style for Art_02_img_6
Art_02_img_6.add_style(style_art_02_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create Art_02_video_1
Art_02_video_1.set_pos(int(28),int(433))
Art_02_video_1.set_size(422,263)
Art_02_video_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_art_02_cont_1_main_main_default
style_art_02_cont_1_main_main_default = lv.style_t()
style_art_02_cont_1_main_main_default.init()
style_art_02_cont_1_main_main_default.set_radius(0)
style_art_02_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_art_02_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_art_02_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_art_02_cont_1_main_main_default.set_bg_opa(255)
style_art_02_cont_1_main_main_default.set_border_color(lv.color_make(0x21,0x95,0xf6))
style_art_02_cont_1_main_main_default.set_border_width(2)
style_art_02_cont_1_main_main_default.set_border_opa(255)
style_art_02_cont_1_main_main_default.set_pad_left(0)
style_art_02_cont_1_main_main_default.set_pad_right(0)
style_art_02_cont_1_main_main_default.set_pad_top(0)
style_art_02_cont_1_main_main_default.set_pad_bottom(0)

# add style for Art_02_cont_1
Art_02_cont_1.add_style(style_art_02_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)



def Art_01_decep_btn_2_clicked_1_event_cb(e,Art_01_hist):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_hist, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_decep_btn_2.add_event_cb(lambda e: Art_01_decep_btn_2_clicked_1_event_cb(e,Art_01_hist), lv.EVENT.CLICKED, None)


def Art_01_decep_btn_1_clicked_1_event_cb(e,Art_01):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_decep_btn_1.add_event_cb(lambda e: Art_01_decep_btn_1_clicked_1_event_cb(e,Art_01), lv.EVENT.CLICKED, None)


def Art_01_decep_btn_4_clicked_1_event_cb(e,Art_02):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_02, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_decep_btn_4.add_event_cb(lambda e: Art_01_decep_btn_4_clicked_1_event_cb(e,Art_02), lv.EVENT.CLICKED, None)


def Art_01_decep_btn_3_clicked_1_event_cb(e,Art_01_inter):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_inter, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_decep_btn_3.add_event_cb(lambda e: Art_01_decep_btn_3_clicked_1_event_cb(e,Art_01_inter), lv.EVENT.CLICKED, None)


def Art_01_hist_btn_1_clicked_1_event_cb(e,Art_01):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_hist_btn_1.add_event_cb(lambda e: Art_01_hist_btn_1_clicked_1_event_cb(e,Art_01), lv.EVENT.CLICKED, None)


def Art_02_btn_1_clicked_1_event_cb(e,Art_01_hist):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_hist, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_02_btn_1.add_event_cb(lambda e: Art_02_btn_1_clicked_1_event_cb(e,Art_01_hist), lv.EVENT.CLICKED, None)


def Art_01_btn_1_clicked_1_event_cb(e,Art_01_hist):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_hist, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_btn_1.add_event_cb(lambda e: Art_01_btn_1_clicked_1_event_cb(e,Art_01_hist), lv.EVENT.CLICKED, None)


def Art_01_hist_btn_3_clicked_1_event_cb(e,Art_01_inter):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_inter, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_hist_btn_3.add_event_cb(lambda e: Art_01_hist_btn_3_clicked_1_event_cb(e,Art_01_inter), lv.EVENT.CLICKED, None)


def Art_01_hist_btn_2_clicked_1_event_cb(e,Art_01_decep):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_decep, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_hist_btn_2.add_event_cb(lambda e: Art_01_hist_btn_2_clicked_1_event_cb(e,Art_01_decep), lv.EVENT.CLICKED, None)


def Art_01_hist_btn_4_clicked_1_event_cb(e,Art_02):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_02, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_hist_btn_4.add_event_cb(lambda e: Art_01_hist_btn_4_clicked_1_event_cb(e,Art_02), lv.EVENT.CLICKED, None)


def Art_01_inter_btn_4_clicked_1_event_cb(e,Art_02):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_02, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_inter_btn_4.add_event_cb(lambda e: Art_01_inter_btn_4_clicked_1_event_cb(e,Art_02), lv.EVENT.CLICKED, None)


def Art_01_inter_btn_1_clicked_1_event_cb(e,Art_01):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_inter_btn_1.add_event_cb(lambda e: Art_01_inter_btn_1_clicked_1_event_cb(e,Art_01), lv.EVENT.CLICKED, None)


def Art_01_inter_btn_3_clicked_1_event_cb(e,Art_01_decep):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_decep, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_inter_btn_3.add_event_cb(lambda e: Art_01_inter_btn_3_clicked_1_event_cb(e,Art_01_decep), lv.EVENT.CLICKED, None)


def Art_01_inter_btn_2_clicked_1_event_cb(e,Art_01_hist):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01_hist, lv.SCR_LOAD_ANIM.FADE_ON, 100, 100, False)
Art_01_inter_btn_2.add_event_cb(lambda e: Art_01_inter_btn_2_clicked_1_event_cb(e,Art_01_hist), lv.EVENT.CLICKED, None)


def Main_scrn_btn_1_clicked_1_event_cb(e,Art_01):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Art_01, lv.SCR_LOAD_ANIM.MOVE_TOP, 100, 100, False)
Main_scrn_btn_1.add_event_cb(lambda e: Main_scrn_btn_1_clicked_1_event_cb(e,Art_01), lv.EVENT.CLICKED, None)


def Main_scrn_imgbtn_1_released_1_event_cb(e,Help_scrn):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Help_scrn, lv.SCR_LOAD_ANIM.MOVE_RIGHT, 100, 100, False)
Main_scrn_imgbtn_1.add_event_cb(lambda e: Main_scrn_imgbtn_1_released_1_event_cb(e,Help_scrn), lv.EVENT.RELEASED, None)


def Help_scrn_imgbtn_1_released_1_event_cb(e,Main_scrn):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(Main_scrn, lv.SCR_LOAD_ANIM.MOVE_LEFT, 100, 100, False)
Help_scrn_imgbtn_1.add_event_cb(lambda e: Help_scrn_imgbtn_1_released_1_event_cb(e,Main_scrn), lv.EVENT.RELEASED, None)



# content from custom.py

# Load the default screen
lv.scr_load(Main_scrn)

while SDL.check():
    time.sleep_ms(5)
