import random
from time import sleep
from dataclasses import dataclass, field


@dataclass(slots=True, kw_only=True)
class Properties:
    name: str = None
    tier: str = None
    position: int = None
    row: int = None
    initial_cost: float = None
    rent_lvl_1_cost: float = None
    rent_lvl_2_cost: float = None
    rent_lvl_3_cost: float = None
    rent_lvl_4_cost: float = None
    rent_lvl_5_cost: float = None
    current_rent_level: int = 1
    current_owner: str = "bank"


# defines a dictionary which contains all the Property class objects for easy access to property attributes by a single number

property_dict = {
    1: Properties(name="Old Kent Road", tier="C", position=2, row=1, initial_cost=60, rent_lvl_1_cost=70, rent_lvl_2_cost=130, rent_lvl_3_cost=220, rent_lvl_4_cost=370, rent_lvl_5_cost=750),
    2: Properties(name="Whitechapel Road", tier="C", position=4, row=1, initial_cost=60, rent_lvl_1_cost=70, rent_lvl_2_cost=130, rent_lvl_3_cost=220, rent_lvl_4_cost=370, rent_lvl_5_cost=750),
    3: Properties(name="The Angel, Islington", tier="C+", position=6, row=1, initial_cost=100, rent_lvl_1_cost=80, rent_lvl_2_cost=140, rent_lvl_3_cost=240, rent_lvl_4_cost=410, rent_lvl_5_cost=800),
    4: Properties(name="Euston Road", tier="C+", position=7, row=1, initial_cost=100, rent_lvl_1_cost=80, rent_lvl_2_cost=140, rent_lvl_3_cost=240, rent_lvl_4_cost=410, rent_lvl_5_cost=800),
    5: Properties(name="Pentonville Road", tier="C+", position=9, row=1, initial_cost=120, rent_lvl_1_cost=100, rent_lvl_2_cost=160, rent_lvl_3_cost=260, rent_lvl_4_cost=440, rent_lvl_5_cost=860),
    6: Properties(name="Pall Mall", tier="B", position=11, row=2, initial_cost=140, rent_lvl_1_cost=110, rent_lvl_2_cost=180, rent_lvl_3_cost=290, rent_lvl_4_cost=460, rent_lvl_5_cost=900),
    7: Properties(name="Whitehall", tier="B", position=13, row=2, initial_cost=140, rent_lvl_1_cost=110, rent_lvl_2_cost=180, rent_lvl_3_cost=290, rent_lvl_4_cost=460, rent_lvl_5_cost=900),
    8: Properties(name="Northumb'nd Avenue", tier="B", position=14, row=2, initial_cost=160, rent_lvl_1_cost=130, rent_lvl_2_cost=200, rent_lvl_3_cost=310, rent_lvl_4_cost=490, rent_lvl_5_cost=980),
    9: Properties(name="Bow Street", tier="B+", position=15, row=2, initial_cost=180, rent_lvl_1_cost=140, rent_lvl_2_cost=210, rent_lvl_3_cost=330, rent_lvl_4_cost=520, rent_lvl_5_cost=1000),
    10: Properties(name="Marlborough Street", tier="B+", position=16, row=2, initial_cost=180, rent_lvl_1_cost=140, rent_lvl_2_cost=210, rent_lvl_3_cost=330, rent_lvl_4_cost=520, rent_lvl_5_cost=1000),
    11: Properties(name="Vine Street", tier="B+", position=18, row=2, initial_cost=200, rent_lvl_1_cost=160, rent_lvl_2_cost=230, rent_lvl_3_cost=350, rent_lvl_4_cost=550, rent_lvl_5_cost=1100),
    12: Properties(name="Strand", tier="A", position=20, row=3, initial_cost=220, rent_lvl_1_cost=170, rent_lvl_2_cost=250, rent_lvl_3_cost=380, rent_lvl_4_cost=580, rent_lvl_5_cost=1160),
    13: Properties(name="Fleet Street", tier="A", position=22, row=3, initial_cost=220, rent_lvl_1_cost=170, rent_lvl_2_cost=250, rent_lvl_3_cost=380, rent_lvl_4_cost=580, rent_lvl_5_cost=1160),
    14: Properties(name="Trafalgar Square", tier="A", position=23, row=3, initial_cost=240, rent_lvl_1_cost=190, rent_lvl_2_cost=270, rent_lvl_3_cost=400, rent_lvl_4_cost=610, rent_lvl_5_cost=1200),
    15: Properties(name="Leicester Square", tier="A+", position=24, row=3, initial_cost=260, rent_lvl_1_cost=200, rent_lvl_2_cost=280, rent_lvl_3_cost=420, rent_lvl_4_cost=640, rent_lvl_5_cost=1300),
    16: Properties(name="Coventry Street", tier="A+", position=25, row=3, initial_cost=260, rent_lvl_1_cost=200, rent_lvl_2_cost=280, rent_lvl_3_cost=420, rent_lvl_4_cost=640, rent_lvl_5_cost=1300),
    17: Properties(name="Piccadilly", tier="A+", position=27, row=3, initial_cost=280, rent_lvl_1_cost=220, rent_lvl_2_cost=300, rent_lvl_3_cost=440, rent_lvl_4_cost=670, rent_lvl_5_cost=1340),
    18: Properties(name="Regent Street", tier="S", position=29, row=4, initial_cost=300, rent_lvl_1_cost=230, rent_lvl_2_cost=320, rent_lvl_3_cost=460, rent_lvl_4_cost=700, rent_lvl_5_cost=1400),
    19: Properties(name="Oxford Street", tier="S", position=31, row=4, initial_cost=300, rent_lvl_1_cost=230, rent_lvl_2_cost=320, rent_lvl_3_cost=460, rent_lvl_4_cost=700, rent_lvl_5_cost=1400),
    20: Properties(name="Bond Street", tier="S", position=32, row=4, initial_cost=320, rent_lvl_1_cost=250, rent_lvl_2_cost=340, rent_lvl_3_cost=480, rent_lvl_4_cost=730, rent_lvl_5_cost=1440),
    21: Properties(name="Park Lane", tier="S+", position=34, row=4, initial_cost=350, rent_lvl_1_cost=270, rent_lvl_2_cost=360, rent_lvl_3_cost=510, rent_lvl_4_cost=740, rent_lvl_5_cost=1500),
    22: Properties(name="Mayfair", tier="S+", position=36, row=4, initial_cost=400, rent_lvl_1_cost=300, rent_lvl_2_cost=400, rent_lvl_3_cost=560, rent_lvl_4_cost=810, rent_lvl_5_cost=1600),
}

tier_sorted_property_dict = {}
row_sorted_property_dict = {}
property_position_dict = {}
for key, obj in property_dict.items():
    common_attr_1 = obj.tier
    common_attr_2 = obj.row

    if common_attr_1 not in tier_sorted_property_dict:
        tier_sorted_property_dict[common_attr_1] = []
    tier_sorted_property_dict[common_attr_1].append(obj.name)

    if common_attr_2 not in row_sorted_property_dict:
        row_sorted_property_dict[common_attr_2] = []
    row_sorted_property_dict[common_attr_2].append(obj.name)

    property_position_dict[obj.position] = obj.name

print(property_dict, tier_sorted_property_dict, row_sorted_property_dict, property_position_dict)


@dataclass(slots=True, kw_only=True)
class Events:
    prompt: str
    event_type: str
