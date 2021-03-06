from cargo import Cargo

cargo = Cargo(id='sulphur',
              type_name='string(STR_CARGO_NAME_SULPHUR)',
              unit_name='string(STR_CARGO_NAME_SULPHUR)',
              type_abbreviation='string(STR_CID_SULPHUR)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='68',
              is_freight='1',
              cargo_classes='bitmask(CC_BULK, CC_LIQUID, CC_COVERED)',
              cargo_label='SULP',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_SULPHUR)',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='102',
              capacity_multiplier='1',
              icon_indices=(13, 3))
