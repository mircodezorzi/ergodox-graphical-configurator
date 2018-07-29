#include QMK_KEYBOARD_H
#include "debug.h"
#include "action_layer.h"
#include "version.h"

enum custom_keycodes{
    EPRM,
    VRSN
    <SEND_KEYS_DECLARATION>
};

<LAYER_DECLARATION>

<MACRO_DECLARATION>

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    <LAYER_DEFINITION>
};

const uint16_t PROGMEM fn_actions[] = {
    [1] = ACTION_LAYER_TAP_TOGGLE(1)
};

const macro_t *action_get_macro(keyrecord_t *record, uint8_t id, uint8_t opt){
    switch(id){
        <MACRO_DEFINITION>
    }
    return MACRO_NONE;
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case EPRM:
            if (record->event.pressed)
                eeconfig_init();
            return false;
            break;
        case VRSN:
            if (record->event.pressed)
                SEND_STRING (QMK_KEYBOARD "/" QMK_KEYMAP " @ " QMK_VERSION);
            return false;
            break;
    }

    if(record->event.pressed){
        switch (keycode){
            <SEND_KEYS_DEFINITION>
        }
      }

    return true;
}

void led_set_user(uint8_t usb_led) {
    if (usb_led & (1<<USB_LED_CAPS_LOCK))
        ergodox_right_led_1_on();
    else
        ergodox_right_led_1_off();
}

void matrix_scan_user(void) {
    uint8_t layer = biton32(layer_state);
    ergodox_board_led_off();
    ergodox_right_led_2_off();
    ergodox_right_led_3_off();
};
