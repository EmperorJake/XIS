from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='copper_mine',
                                     prod_cargo_types=['CORE'],
                                     prob_in_game='4',
                                     prob_random='7',
                                     prod_multiplier='[20, 0]',
                                     map_colour='10',
                                     location_checks=dict(cluster=[60, 3]),
                                     prospect_chance='0.75',
                                     name='TTD_STR_INDUSTRY_NAME_COPPER_ORE_MINE',
                                     nearby_station_name='string(STR_STATION_COPPER_LODE)',
                                     fund_cost_multiplier='238',
                                     intro_year=1800)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='copper_mine_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'  # ground tile same as overlay tile
)

spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 110, -31, -70)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -31)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -31)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -31)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -31)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=8,
    yoffset=2,
    zoffset=70,
)

industry.add_spritelayout(
    id='copper_mine_spritelayout_chimney',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_large_shed',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_conveyors',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_processor',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_raised_tanks',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_raised_shed',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_machinery',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_hut',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
     
)
industry.add_spritelayout(
    id='copper_mine_spritelayout_empty',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
     
)

industry.add_industry_layout(
    id='copper_mine_industry_layout_1',
    layout=[(0, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_chimney'),
            (0, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_raised_shed'),
            (0, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_hut'),
            (1, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_raised_tanks'),
            (1, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_raised_tanks'),
            (1, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_empty'),
            (2, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_processor'),
            (2, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_processor'),
            (2, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_empty'),
            (3, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_conveyors'),
            (3, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_conveyors'),
            (3, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_empty'),
            (4, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_large_shed'),
            (4, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_large_shed'),
            (4, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_machinery'),
            ]
)
industry.add_industry_layout(
    id='copper_mine_industry_layout_2',
    layout=[(0, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_raised_tanks'),
            (0, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_processor'),
            (0, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_processor'),
            (0, 3, 'copper_mine_tile_1', 'copper_mine_spritelayout_raised_shed'),
            (1, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_chimney'),
            (1, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_conveyors'),
            (1, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_conveyors'),
            (1, 3, 'copper_mine_tile_1', 'copper_mine_spritelayout_empty'),
            (2, 0, 'copper_mine_tile_1', 'copper_mine_spritelayout_machinery'),
            (2, 1, 'copper_mine_tile_1', 'copper_mine_spritelayout_large_shed'),
            (2, 2, 'copper_mine_tile_1', 'copper_mine_spritelayout_large_shed'),
            (2, 3, 'copper_mine_tile_1', 'copper_mine_spritelayout_hut'),
            ]
)
