import reservation
import make_reservation
import delete_reservation
import search_reservation
import checkin
import checkout
import guest_list
import settings
import price_calc
import addrooms
import addroom_list
import addroom_type
import removerooms
import removeroom_list
import removeroom_type


def init():
    global reserve_window
    global make_reservation_window 
    global delete_reservation_window 
    global search_reservation_window 
    global checkin_window 
    global checkout_window 
    global guestlist_window
    global settings_window 
    global pricecalc_window
    global addrooms_window
    global addroom_list_window
    global addroom_type_window
    global removerooms_window
    global removeroom_list_window
    global removeroom_type_window

    reserve_window = reservation.reserve(hide = True)
    make_reservation_window = make_reservation.make_reserve(hide = True)
    delete_reservation_window = delete_reservation.delete_reserve(hide = True)
    search_reservation_window = search_reservation.search_reserve(hide = True)
    checkin_window = checkin.checkin(hide = True)
    checkout_window = checkout.checkout(hide = True)
    guestlist_window = guest_list.guest_list(hide = True)
    settings_window = settings.settings(hide = True)
    pricecalc_window = price_calc.price_calc(hide = True)
    addrooms_window = addrooms.addrooms(hide = True)
    addroom_list_window = addroom_list.addroom_list(hide = True)
    addroom_type_window = addroom_type.addroom_type(hide = True)
    removerooms_window = removerooms.removerooms(hide = True)
    removeroom_list_window = removeroom_list.removeroom_list(hide = True)
    removeroom_type_window = removeroom_type.removeroom_type(hide = True)