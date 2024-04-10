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
    base_rent_levels_list: list = field(init=False)
    current_rent_level: int = 1
    current_owner: str = "bank"
    
    def __post_init__(self):
        self.base_rent_levels_list = [(round(((self.initial_cost*i/8) + ((round(self.initial_cost*((i/7)**2)/10))*10))/10)*10) for i in range(5,14,2)]
    
    def __lt__(self, other):
        if not isinstance(other, Properties):
            raise ValueError("Comparison with incompatible type")
        return self.initial_cost < other.initial_cost

    def __gt__(self, other):
        if not isinstance(other, Properties):
            raise ValueError("Comparison with incompatible type")
        return self.initial_cost > other.initial_cost
    
    def __eq__(self, other):
        if not isinstance(other, Properties):
            raise ValueError("Comparison with incompatible type")
        return self.initial_cost == other.initial_cost
            
        


# defines a dictionary which contains all the Property class objects for easy access to property attributes by a single number

def property_creation():
    
    temp_property_list = [
        Properties(name="Old Kent Road", initial_cost=60),
        Properties(name="Whitechapel Road", initial_cost=80),
        Properties(name="The Angel, Islington", initial_cost=100),
        Properties(name="Euston Road", initial_cost=110),
        Properties(name="Pentonville Road", initial_cost=130),
        Properties(name="Pall Mall", initial_cost=140),
        Properties(name="Whitehall", initial_cost=150),
        Properties(name="Northumb'nd Avenue", initial_cost=160),
        Properties(name="Bow Street", initial_cost=170),
        Properties(name="Marlborough Street", initial_cost=180),
        Properties(name="Vine Street", initial_cost=200),
        Properties(name="Strand", initial_cost=220),
        Properties(name="Fleet Street", initial_cost=230),
        Properties(name="Tra falgar Square", initial_cost=240),
        Properties(name="Leicester Square", initial_cost=250),
        Properties(name="Coventry Street", initial_cost=260),
        Properties(name="Piccadilly", initial_cost=280),
        Properties(name="Regent Street", initial_cost=300),
        Properties(name="Oxford Street", initial_cost=310),
        Properties(name="Bond Street", initial_cost=320),
        Properties(name="Park Lane", initial_cost=350),
        Properties(name="Mayfair", initial_cost=400)
        ]
    
    temp_property_list.sort()
    property_names_list = [obj.name for obj in temp_property_list]
    temp_property_list_tiered = []
    i = 0
    j = 2
    k = 0
    while True:
        temp_property_list_tiered.append(property_names_list[i:j])
        i = j
        
        if k % 2 == 0:
            j += 3
        
        elif k % 2 == 1:
            j += 4
        
        k += 1
        
        if j > len(property_names_list) - 1:
            j = len(property_names_list) - 1
            temp_property_list_tiered.append(property_names_list[i:j])
            break
        
        elif j == len(property_names_list) - 1:
            break
    
    def tier_generator(length, alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
        tier_list = []
        for i in range(length):
            index = ""
            remainder = i
            while remainder >= 0:
                index = (alphabet[remainder % 26] + index).upper()
                remainder = remainder // 26 - 1
            tier_list.append(index)
        return tier_list
    
    tier_list = tier_generator(len(temp_property_list_tiered))
    mod_tier_list = ["S+", "S"]
    for tier in tier_list:
        mod_tier_list.append(tier + "+")
        mod_tier_list.append(tier)
    tier_list = mod_tier_list[:len(temp_property_list_tiered)]
    tier_list = tier_list[::-1]
    tier_sorted_property_dict = {}
    for list_of_objects, tier in zip(temp_property_list_tiered, tier_list):           
        tier_sorted_property_dict[tier] = list_of_objects
        
    print(tier_sorted_property_dict)
    '''
    property_dict = {
        1: Properties(name="Old Kent Road", initial_cost=60),
        2: Properties(name="Whitechapel Road", initial_cost=80),
        3: Properties(name="The Angel, Islington", initial_cost=100),
        4: Properties(name="Euston Road", initial_cost=110),
        5: Properties(name="Pentonville Road", initial_cost=130),
        6: Properties(name="Pall Mall", initial_cost=140),
        7: Properties(name="Whitehall", initial_cost=150),
        8: Properties(name="Northumb'nd Avenue", initial_cost=160),
        9: Properties(name="Bow Street", initial_cost=170),
        10: Properties(name="Marlborough Street", initial_cost=180),
        11: Properties(name="Vine Street", initial_cost=200),
        12: Properties(name="Strand", initial_cost=220),
        13: Properties(name="Fleet Street", initial_cost=230),
        14: Properties(name="Trafalgar Square", initial_cost=240),
        15: Properties(name="Leicester Square", initial_cost=250),
        16: Properties(name="Coventry Street", initial_cost=260),
        17: Properties(name="Piccadilly", initial_cost=280),
        18: Properties(name="Regent Street", initial_cost=300),
        19: Properties(name="Oxford Street", initial_cost=310),
        20: Properties(name="Bond Street", initial_cost=320),
        21: Properties(name="Park Lane", initial_cost=350),
        22: Properties(name="Mayfair", initial_cost=400),
    }
    '''
    ''' 
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
    '''

property_creation()

@dataclass(slots=True, kw_only=True)
class Events:
    prompt: str
    event_type: str
