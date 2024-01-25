
LOCATION_CHOICES = (
        ('KL', 'Kili'),
        ('KM', 'Kighali_kaghumo'),
        ('KW', 'Kisembwe'),
        ('KS', 'Kipese'),
        ('BB', 'Butembo'),
        ('KK', 'Kasiki'),
        ('KI', 'Kighali_Vitula'),
        ('LZ', 'Locataire_Nziapanda'),
        ('OT', 'Other'),
    )


ACCOUNT_CHOICES = (
    ('Bureau_Central', 'Bureau_Central'), 
    ('Katembo_Syalivene', 'Katembo_Syalivene'), 
    ('Kasereka_Kavatsi', 'Kasereka_Kavatsi'), 
    ('Kahindo_Vikoma', 'Kahindo_Vikoma'), 
    )

UNIT_CHOICES = (
    ('SC', 'Sac'),
    ('TG', 'Tige'),
    ('BX', 'Box'),
    ('OT', 'Autre'),
)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )


POSITION_CHOICES = (
        ('E', 'Boss'),
        ('A', 'Agent Bureau'),
        ('B', 'Ouvrier'),
        ('E', 'Locataire_nziapanda'),
        ('F', 'Locataire_Kasiki'),
        ('C', 'Collaborateur'),
        ('D', 'Autre'),
    )


TYPE_CHOICES_1 = (
        ('F', 'Fixed'),
        ('C', 'Consumable'),
        ('R', 'Renewable'),
        ('N', 'Non-renewable'),
        ('O', 'Other'),
    )


JUSTIFICATION_CHOICES = (
        ('AV', 'Salaire'),
        ('AL', 'Loyer'),
    )


TYPE_CHOICES_3 = (
        ('IP', 'Arrivage'),
        ('OP', 'Vente'),
        ('OT', 'Achat'),
    )

TYPE_CHOICES_2 = (
        ('IP', 'Input'),
        ('OP', 'Output'),
    )