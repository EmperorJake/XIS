from cargo import Cargo

cargo = Cargo(id='steel',
              type_name='string(STR_CARGO_NAME_STEEL)',
              unit_name='string(STR_CARGO_NAME_STEEL)',
              type_abbreviation='string(STR_CID_STEEL)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='10',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS)',
              cargo_label='STEL',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_STEEL)',
              penalty_lowerbound='14',
              single_penalty_length='255',
              capacity_multiplier='1',
              price_factor='126',
              icon_indices=(10, 0))
