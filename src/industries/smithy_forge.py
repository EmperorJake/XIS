from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='smithy_forge',
                             processed_cargos_and_output_ratios=[('ACID', 2), ('COPR', 4), ('KAOL', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['POWR', 'GOOD'],
                             prob_in_game='2',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='143',
                             name='string(STR_IND_BATTERY_PLANT)',
                             nearby_station_name='string(STR_STATION_BATTERY_PLANT)',
                             fund_cost_multiplier='63',
                             intro_year=1890)

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='smithy_forge_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -49)],
)
# spriteset_2 was deprecated
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 80, -31, -49)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 80, -31, -49)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 80, -31, -49)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 80, -31, -49)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 80, -31, -49)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 80, -31, -49)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 80, -31, -49)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 80, -31, -49)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 80, -31, -49)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(640, 100, 64, 80, -31, -49)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='dark_smoke_small',
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id='smithy_forge_spritelayout_rear_assembly_hall_windows',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_central_assembly_hall',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_front_assembly_hall_windows',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_front_assembly_hall_doors',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_goods_in_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_offices',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_tyres',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_vehicles_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_vehicles_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
     
)
industry.add_spritelayout(
    id='smithy_forge_spritelayout_vehicles_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_12],
     
)

industry.add_industry_layout(
    id='smithy_forge_industry_layout_1',
    layout=[(0, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_rear_assembly_hall_windows'),
            (0, 1, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_central_assembly_hall'),
            (0, 2, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_front_assembly_hall_doors'),
            (0, 3, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_1'),
            (1, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_rear_assembly_hall_windows'),
            (1, 1, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_central_assembly_hall'),
            (1, 2, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_front_assembly_hall_windows'),
            (1, 3, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_2'),
            (2, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_rear_assembly_hall_windows'),
            (2, 1, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_central_assembly_hall'),
            (2, 2, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_front_assembly_hall_doors'),
            (2, 3, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_1'),
            (3, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_offices'),
            (3, 1, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_offices'),
            (3, 2, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_tyres'),
            (3, 3, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_2'),
            (4, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_goods_in_1'),
            (4, 1, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_tyres'),
            (4, 2, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_3'),
            (4, 3, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_vehicles_3'),
            ]
)
