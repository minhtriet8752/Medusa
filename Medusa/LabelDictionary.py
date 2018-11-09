#### This File Contains Dictionaries and Helpers ######
## its goal is to make labels human-readble,
## and help us to map gtsrb -> gi Label and vice versa


### Original GTSRB #####
### Yes, its englisch ... ### 
GTSRB_INT_TO_LABEL = {
    '0': '20_speed',
    '1': '30_speed',
    '2': '50_speed',
    '3': '60_speed',
    '4': '70_speed',
    '5': '80_speed',
    '6': '80_lifted',
    '7': '100_speed',
    '8': '120_speed',
    '9': 'no_overtaking_general',
    '10': 'no_overtaking_trucks',
    '11': 'right_of_way_crossing',
    '12': 'right_of_way_general',
    '13': 'give_way',
    '14': 'stop',
    '15': 'no_way_general',
    '16': 'no_way_trucks',
    '17': 'no_way_one_way',
    '18': 'attention_general',
    '19': 'attention_left_turn',
    '20': 'attention_right_turn',
    '21': 'attention_curvy',
    '22': 'attention_bumpers',
    '23': 'attention_slippery',
    '24': 'attention_bottleneck',
    '25': 'attention_construction',
    '26': 'attention_traffic_light',
    '27': 'attention_pedestrian',
    '28': 'attention_children',
    '29': 'attention_bikes',
    '30': 'attention_snowflake',
    '31': 'attention_deer',
    '32': 'lifted_general',
    '33': 'turn_right',
    '34': 'turn_left',
    '35': 'turn_straight',
    '36': 'turn_straight_right',
    '37': 'turn_straight_left',
    '38': 'turn_right_down',
    '39': 'turn_left_down',
    '40': 'turn_circle',
    '41': 'lifted_no_overtaking_general',
    '42': 'lifted_no_overtaking_trucks'
}


### Read from Mongo 
### See Database/GetAllClasses.txt for the simple how-to
MONGO_LBL=[
        "Ende aller Streckenverbote",
        "Gefahrenstelle",
        "Rechts vorbei",
        "Vorfahrt gewähren",
        "Zulässige Höchstgeschwindigkeit (30)",
        "Zulässige Höchstgeschwindigkeit (20)",
        "Zulässige Höchstgeschwindigkeit (50)",
        "Zulässige Höchstgeschwindigkeit (70)",
        "Baustelle",
        "Überholverbot für Kraftfahrzeuge mit einer zulässigen Gesamtmasse über 3,5t",
        "Vorfahrt",
        "Einmalige Vorfahrt",
        "Verbot der Einfahrt",
        "Kurve (links)",
        "Ende des Überholverbotes für Kraftfahrzeuge mit einer zulässigen Gesamtmasse über 3,5t",
        "Verbot für Kraftfahrzeuge mit einer zulässigen Gesamtmasse von 3,5t",
        "Kreisverkehr",
        "Zulässige Höchstgeschwindigkeit (60)",
        "Wildwechsel",
        "Ausschließlich geradeaus",
        "Kurve (rechts)",
        "Schleudergefahr bei Nässe oder Schmutz",
        "Ende des Überholverbotes für Kraftfahrzeuge aller Art",
        "Links vorbei",
        "Fahrradfahrer",
        "Zulässige Höchstgeschwindigkeit (100)",
        "Zulässige Höchstgeschwindigkeit (80)",
        "Ausschließlich rechts",
        "Überholverbot für Kraftfahrzeuge aller Art",
        "Doppelkurve (zunächst links)",
        "Verbot für Fahrzeuge aller Art",
        "Fußgänger",
        "Unebene Fahrbahn"
        ]

