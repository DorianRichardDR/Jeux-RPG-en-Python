import os
import random

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')



class Monster:
    MONSTERS = {
        'Slime': {'PV': 12,
            'Skills': {'Mouille': {'ATK' : 4, 'hit': 0.7},
                    'Coup de boule' : {'ATK' : 5, 'hit' : 0.7}}},
        'Squelette': {'PV': 14,
            'Skills': {'Koudos': {'ATK' : 5, 'hit': 0.75},
                    'Grinços' : {'ATK' : 6, 'hit' : 0.6}}},
        'Gobelin': {'PV': 16,
            'Skills': {'Coup de poignard': {'ATK' : 6, 'hit': 0.70},
                    'Coup de poing' : {'ATK' : 5, 'hit' : 0.8}}},
        'Loup': {'PV': 18,
            'Skills': {'Morsure': {'ATK' : 8, 'hit': 0.80},
                    'Griffure' : {'ATK' : 7, 'hit' : 0.9}}},
        'Timmy': {'PV': 20,
            'Skills': {'Ecrasement de tête': {'ATK' : 2, 'hit': 1},
                    'Roulage latéral' : {'ATK' : 2, 'hit' : 1}}},
        'Gang de gobelins': {'PV': 22,
            'Skills': {'Koudos': {'ATK' : 5, 'hit': 0.75},
                    'Grinços' : {'ATK' : 6, 'hit' : 0.6}}},
        'Gang de squelettes': {'PV': 28, 
            'Skills': {'Attaque de fémur': {'ATK': 7, 'hit': 0.6},
                    'Lancer de dents': {'ATK': 5, 'hit': 0.9}}},
        'Troll': {'PV': 25,
            'Skills': {'Coup de masse': {'ATK': 10, 'hit': 0.5},
                    'Attaque en puissance': {'ATK': 8, 'hit': 0.8}}},
        'Loup Géant': {'PV': 30,
            'Skills': {'Morsure suprême': {'ATK': 11, 'hit': 0.7},
                    'Coup de queue': {'ATK': 8, 'hit': 0.9}}},
        'Dragon': {'PV': 40, 'Boss': True,
            'Skills': {'Hurlement suprême': {'ATK': 12, 'hit': 0.9},
                    'Brasier mortel': {'ATK': 14, 'hit': 0.5}}}
    }

    def __init__(self, name) -> None:
        self.name = name
        self.PV = self.MONSTERS.get(self.name).get('PV')

    def get_skills(self):
        return list(self.MONSTERS.get(self.name).get('Skills').keys())

    def lose_PV(self, dmg):
        self.PV = self.PV - dmg

    def is_dead(self):
        return self.PV <= 0

    def is_boss(self):
        return self.MONSTERS.get(self.name).get('Boss')

    def get_skill(self, skill):
        return self.MONSTERS.get(self.name).get('Skills').get(skill)
            
    def get_random_skill_name(self):   
        return random.choice(self.get_skills())

    def get_dmg(self, skill):
        return self.get_skill(skill).get('ATK')

class Items:
    ITEMS = {
        'Potion de Vie':{'Redonne 20 PV'},
        'Potion de Force':{'Confère +4 ATK pour un combat'},
        'Potion de Défense':{'Confère +2 DEF pour un combat'},
        'Epée Simple':{'+2 ATK'},
        'Epée très grosse':{'+5 ATK'},
        'Tueuse de Dragon':{'+10 ATK'},
        'Cotte de maille':{'+3 DEF'},
        'Armure en acier':{'+5 DEF'},
        'Seringue étrange':{'+10 PV' : 0.5, '-10 PV' : 0.5},
        'Clé Inutile':{'Une clé qui ne sert probablement à rien'},
        'Diamant':{'Un diamant d\'une grande valeur'}
    }



class World:
    ZONE_PLAINE_SAUVAGE = 'la Plaine sauvage'
    ZONE_FORET = 'la Forêt'
    ZONE_MAUSOLEE = 'le Mausolée'

    ROOMS = {
        '0': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '1', 'objet':'Epée Simple'},
        '1': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '2', 'Sud': '0', 'objet': 'Clé Inutile'},
        '2': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '8', 'Sud': '1', 'est': '5', 'ouest': '3'},
        '3': {'zone': ZONE_PLAINE_SAUVAGE, 'Est': '2', 'Ouest': '4'},
        '4': {'zone': ZONE_PLAINE_SAUVAGE, 'Est': '3', 'objet': 'Diamant'},
        '5': {'zone': ZONE_PLAINE_SAUVAGE, 'Est': '6', 'Ouest': '2', 'monster': 'Squelette'},
        '6': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '7', 'Ouest': '5', 'objet': 'Armure'},
        '7': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '11', 'Sud': '6'},
        '8': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '9', 'Sud': '2', 'monster': 'Gobelin'},
        '9': {'zone': ZONE_PLAINE_SAUVAGE, 'Sud': '8', 'Est': '10'},
        '10': {'zone': ZONE_PLAINE_SAUVAGE, 'Est': '11', 'Ouest': '9', 'monster': 'Timmy'},
        '11': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '12', 'Sud': '7', 'Ouest': '10', 'monster': 'Loup'},
        '12': {'zone': ZONE_PLAINE_SAUVAGE, 'Nord': '18', 'Sud': '11', 'Est': '13'},
        '13': {'zone': ZONE_PLAINE_SAUVAGE, 'Est': '12', 'Ouest': '14','objet': 'Potion De Vie'},
        '14': {'zone': ZONE_FORET, 'Nord': '15', 'Ouest': '13','rencontre' : 'Bébé Dragon'},
        '15': {'zone': ZONE_FORET, 'Nord': '16', 'Sud': '14', 'monster' : 'Gang de squelettes'},
        '16': {'zone': ZONE_FORET, 'Nord': '17', 'Sud': '15', 'objet' : 'Potion de Force'},
        '17': {'zone': ZONE_FORET, 'Sud': '16', 'Ouest': '21', 'rencontre' : 'Marchand'},
        '18': {'zone': ZONE_FORET, 'Nord': '19', 'Sud': '12', 'monster' : 'Gang de gobelins'},
        '19': {'zone': ZONE_FORET, 'Nord': '20', 'Sud': '18'},
        '20': {'zone': ZONE_FORET, 'Sud': '19','Est' : '21'},
        '21': {'zone': ZONE_FORET, 'Nord':'22', 'Est': '20','ouest' : '17'},
        '22': {'zone': ZONE_MAUSOLEE, 'Sud': '21','Nord' : '23'},
        '23': {'zone': ZONE_MAUSOLEE, 'Nord': '25', 'Sud': '22','Ouest' : '24', 'monster' : 'Loup Géant'},
        '24': {'zone': ZONE_MAUSOLEE, 'Est' : '21', 'objet' : 'Tueuse De Dragon'},
        '25': {'zone': ZONE_MAUSOLEE, 'Sud': '22', 'monster' : 'Dragon'},

        
    }

    def __init__(self) -> None:
        self.current_room = self.ROOMS['0']

    def get_current_room(self):
        return self.current_room

    def get_current_room_directions(self):
        directions = []
        if self.current_room.get('Nord'):
            directions.append('Nord')
        if self.current_room.get('Sud'):
            directions.append('Sud')
        if self.current_room.get('Est'):
            directions.append('Est')
        if self.current_room.get('Ouest'):
            directions.append('Ouest')
        
        return directions

    def go_to_next_room(self, direction):
        """
        direction: 'nord', 'sud', 'est, 'ouest'
        """
        next_room_number = self.current_room.get(direction)
        self.current_room = self.ROOMS[next_room_number]
        
        return self.current_room

    def get_current_room_zone(self):
        return self.current_room.get('zone')
    
    def get_current_room_object(self):
        return self.current_room.get('objet')

    def get_current_room_monster(self):
        return self.current_room.get('monster')


class Player:
    PLAYER_ROLES = {
        'Guerrier': {'PV': 35, 'DEF': 6, 
            'skills': {'Coup de poing': {'ATK': 8, 'hit': 0.8},
                    'Coup d\'épée': {'ATK': 14, 'hit': 0.75}}},
        'Paladin': {'PV': 40, 'DEF': 8,
            'skills': {'Coup d\'épaule': {'ATK': 6, 'hit': 0.8},
                    'Coup d\'épée': {'ATK': 12, 'hit': 0.75}}},
        'Assassin': {'PV': 270, 'DEF': 5,
            'skills': {'Coup de pieds': {'ATK': 10, 'hit': 0.8},
                    'Coup d\'épée': {'ATK': 16, 'hit': 0.75}}},
    }

    def __init__(self, name) -> None:
        self.name = name
        self.role = None
        self.PV = None
        self.items = []

    def get_roles(self):
        return list(self.PLAYER_ROLES.keys())

    def set_role(self, role):
        self.role = role
        self.PV = self.PLAYER_ROLES.get(self.role).get('PV')

    def get_skills(self):
        return self.PLAYER_ROLES.get(self.role).get('skills')

    def get_skill(self, skill):
        return self.get_skills().get(skill)
    
    def get_dmg(self, skill):
        return self.get_skill(skill).get('ATK')

    def lose_PV(self, dmg):
        self.PV = self.PV - dmg

    def is_dead(self):
        return self.PV <= 0



class Game:
    def __init__(self) -> None:
        self.player = None
        self.world = None
        self.game_over = False

    def run(self):
       while True:
            self.display_menu()
            choice = input('Choisissez une option : ')

            if choice == '1':
               self.start_game()
           
            if choice == '2':
                clear_screen()
                print('___________________________\n')
                print('Option indisponible')
                print('___________________________\n')

            if choice == '3':
                clear_screen()
                print('___________________________\n')
                print('Bienvenue dans le monde de Dragon oklm dans la foret, monde semi-fantaisie semi-social, si vous rencontrer timmy est en fauteuil roulant.')
                print('___________________________\n')

            if choice == '4':
               break


    def display_menu(self):
        print('')
        print('---DRAGON OKLM DANS LA FORÊT---\n')
        print('1. Nouvelle partie')
        print('2. Reprendre la partie (non-disponble)')
        print('3. À propos (Ya rien)')
        print('4. Quitter le jeu')
        print('___________________________\n')

    def start_game(self):
        
        self.world = World()
        print('___________________________\n')
        name = input('Quel est votre nom ? ')
        print('___________________________\n')
        self.player = Player(name)

        self.player.set_role(self.ask_user_player_role())
        clear_screen()
        print('_______________________________________________________________________________________________________________\n')

        print(f'Bonjour {self.player.role} {name}, un dragon vit dans un mausolée un peu plus loin, prenez cette épée allez l\'occir !')
        print('_______________________________________________________________________________________________________________\n')
        
        while True:
            current_zone = self.world.get_current_room_zone()
            
            monster_name = self.world.get_current_room_monster()
            if monster_name:
                self.start_battle(monster_name)
                if self.player.is_dead() or self.game_over:
                    break

            objet = self.world.get_current_room_object()
            if objet:
                print('___________________________\n')
                print(f'Objet Trouvé: {objet}')
                print('___________________________\n')
            
            if not monster_name and not objet:
                print('___________________________\n')
                print('La pièce est vide')
                print('___________________________\n')
            direction = self.ask_user_next_direction()
            self.world.go_to_next_room(direction)

            new_zone = self.world.get_current_room_zone()
            if new_zone != current_zone:
                print('___________________________\n')
                print(f'Vous arrivez dans {new_zone}')
                print('___________________________\n')


    def ask_user_player_role(self):
        clear_screen()
        # roles : ['Guerrier', 'Paladin', 'Assassin']
        roles = self.player.get_roles()
        print('___________________________\n')
        print('Classes possibles:')
        print('___________________________\n')
        for idx, role in enumerate(roles):
            print(f'- {idx+1} : {role}')
        
        role = None

        while not role:  
            print('\n')      
            number_str = input(f'Choisissez votre classe : ')
            
            try:
                role = roles[int(number_str)-1]
            except:
                print('Valeur incorrecte !')

        return role


    def ask_user_next_direction(self):
        room_directions = self.world.get_current_room_directions()
        print('Directions possibles:')
        print('\n')

        for idx, direction in enumerate(room_directions):
            print(f'- {idx+1} : {direction}')

            
        direction = None

        while not direction: 
            print('\n')
            number_str = input(f'Choisir une direction : ')
            try:
                direction = room_directions[int(number_str)-1]
            except:
                print('Valeur incorrecte !')
        
        clear_screen()
        
        
        
        return direction

    def start_battle(self, monster_name):
        monster = Monster(monster_name)
        print('______________________________________________________\n')
        print(f'Vous  êtes attaqué par un monstre !')
        print(f'Début du combat contre {monster.name} (PV:{monster.PV})  ')
        print('______________________________________________________\n')
        
        
        while True:
            print(f'PV Actuels : {self.player.PV}\n')
            print('1. Attaque')
            print('2. Magie (non-disponible)')
            print('3. Objet (non-disponible)')
            print('4. Fuite')
            print('___________________________\n')
            choice = input('Que voulez vous faire ? ')
            if choice == '1':
                self.start_attack(monster)
                if monster.is_dead() or self.player.is_dead() or self.game_over:
                    break
                 
            if choice == '2':
                clear_screen()
                print('___________________________\n')
                print('Option indisponible')
                print('___________________________\n')
            
            if choice == '3':  
                clear_screen()
                print('___________________________\n')
                print('Option indisponible')
                print('___________________________\n')  

            if choice == '4':
                clear_screen()
                print('___________________________\n')
                print('Fuite impossible')
                print('___________________________\n')
                
            

    def start_attack(self, monster: Monster):
            player_skill = self.choose_skill()
        
            monster.lose_PV(self.player.get_dmg(player_skill))
            if monster.is_dead():
                print('___________________________\n')
                print(f'Le {monster.name} a été vaincu !')
                print('___________________________\n')
                if monster.is_boss():
                    print('Bravo ! Vous avez vaincu le  !')
                    print('Partie terminée')
                    self.game_over = True
            else :
                print('___________________________\n')
                print(f'Vous infligez {self.player.get_dmg(player_skill)} dégats à {monster.name} !\n')
                print(f'Il lui reste encore {monster.PV} PV !')
                monster_skill = monster.get_random_skill_name()
                self.player.lose_PV(monster.get_dmg(monster_skill))
                print('___________________________\n')
                print(f'{monster.name} utilise {monster_skill} ce qui vous inflige {monster.get_dmg(monster_skill)} de dégats !')
                print('___________________________\n')
                if self.player.is_dead():

                    print('Vous êtes mort, retour au menu principal...')
                    print('===========================================\n')

                    
    
    def choose_skill(self):
        skills = list(self.player.get_skills().keys())
        print('___________________________\n')
        for idx, skill in enumerate(skills):
            print(f'- {idx+1} : {skill}')
        
        skill = None

        while not skill: 
            print('___________________________\n')       
            number_str = input(f'Choisissez une attaque : ')
            try:
                skill = skills[int(number_str)-1]
            except:
                print('Valeur incorrecte !')
        clear_screen()
        return skill

    def continue_game(self):
        print('game started')

    def about(self):
        print('about')




def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
