import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock

kivy.require('2.1.0')

class MyApp(App):
    def build(self):

        layout = FloatLayout(size=(800, 600))


        background_image = Image(source='fundomodificado.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background_image)

        enemy_image2 = Image(source='timeA/Acentral.png', size_hint=(None, None), size=(100, 100), pos=(-2, 159))
        layout.add_widget(enemy_image2)

        enemy_image3 = Image(source='timeA/Alevantador.png', size_hint=(None, None), size=(100, 100), pos=(73, 268))
        layout.add_widget(enemy_image3)

        enemy_image4 = Image(source='timeA/Alibero.png', size_hint=(None, None), size=(100, 100), pos=(111, 358))
        layout.add_widget(enemy_image4)

        enemy_image5 = Image(source='timeA/Aoposto.png', size_hint=(None, None), size=(100, 100), pos=(231, 356))
        layout.add_widget(enemy_image5)

        enemy_image6 = Image(source='timeA/Aponteiro1.png', size_hint=(None, None), size=(100, 100), pos=(233, 272))
        layout.add_widget(enemy_image6)

        enemy_image7 = Image(source='timeA/Aponteiro2.png', size_hint=(None, None), size=(100, 100), pos=(211, 187))
        layout.add_widget(enemy_image7)

        enemy_image8 = Image(source='timeB/Bcentral.png', size_hint=(None, None), size=(100, 100), pos=(311, 355))
        layout.add_widget(enemy_image8)

        enemy_image9 = Image(source='timeB/Blevantador.png', size_hint=(None, None), size=(100, 100), pos=(421, 354))
        layout.add_widget(enemy_image9)

        enemy_image10 = Image(source='timeB/Blibero.png', size_hint=(None, None), size=(100, 100), pos=(455, 282))
        layout.add_widget(enemy_image10)

        enemy_image11 = Image(source='timeB/Boposto.png', size_hint=(None, None), size=(100, 100), pos=(416, 184))
        layout.add_widget(enemy_image11)

        enemy_image12 = Image(source='timeB/Bponteiro1.png', size_hint=(None, None), size=(100, 100), pos=(309, 185))
        layout.add_widget(enemy_image12)

        enemy_image13 = Image(source='timeB/Bponteiro2.png', size_hint=(None, None), size=(100, 100), pos=(307, 268))
        layout.add_widget(enemy_image13)


        self.ball_image = Image(source='bola.png', size_hint=(None, None), size=(100, 100), pos=(63 - 47, 212 - 52))
        layout.add_widget(self.ball_image)


        self.button1 = Button(text='Saque', size_hint=(0.19, 0.1), pos_hint={'right': 0.99, 'top': 0.9})
        self.button2 = Button(text='Ataque', size_hint=(0.19, 0.1), pos_hint={'right': 0.99, 'top': 0.7})
        self.button3 = Button(text='Próxima Rotação', size_hint=(0.19, 0.1), pos_hint={'right': 0.99, 'top': 0.5})


        self.button1.bind(on_press=self.on_serve_button_press)
        self.button2.bind(on_press=self.on_attack_button_press)
        self.button3.bind(on_press=self.on_next_rotation_button_press)

        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)



        Window.bind(on_touch_down=self.on_touch_down)


        self.next_serve_path = 1


        self.next_attack_path = 1


        self.next_rotation_path = 1

        return layout

    def on_serve_button_press(self, instance):

        serve_paths = {
            1: {#Ajeitado
                'bola.png': {'coordinates': [(18,157),(397, 274), (306, 267)], 'speed': 4},
                'timeA/Alibero.png': {'coordinates': [(112,354)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(397, 274)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(-1,159),(113, 184)], 'speed': 2},

                'timeA/Alevantador.png': {'coordinates': [(75, 268)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(232, 271)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(214, 184)], 'speed': 2},

                'timeB/Bcentral.png': {'coordinates': [(312, 354)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(307, 267)], 'speed': 2},
                'timeB/Bponteiro.png': {'coordinates': [(113, 184)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(423, 354)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(416, 183)], 'speed': 2},


            },
            2: {#Ajeitado
                'bola.png': {'coordinates': [(132, 269), (240, 274)], 'speed': 3},
                'timeB/Blevantador.png': {'coordinates': [(458, 284)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(423, 356)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(416, 183)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(311, 184)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(307, 266)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(310, 356)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(131, 271)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(98, 184)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(113, 355)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(190, 378)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(240, 275)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(188, 165)], 'speed': 2},
            },
            3: {#Ajeitado
                'bola.png': {'coordinates': [(434,278),(307, 262)], 'speed': 3.6},
                'timeB/Blibero.png': {'coordinates': [(394, 228)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(109, 186)], 'speed': 2},
            },
            4: {  # Ajeitado
                'bola.png': {'coordinates': [(119, 353), (233, 276)], 'speed': 3.6},
                'timeB/Bponteiro1.png': {'coordinates': [(423, 358)], 'speed': 2},
            },
            5:{
                'bola.png': {'coordinates': [(444, 278), (306, 273)], 'speed': 3.6},
                'timeA/Aponteiro1.png': {'coordinates': [(120, 177)], 'speed': 2},

            },
            6:{

            },

        }
        if self.next_serve_path == 6:
             self.next_serve_path = 1


        path_data = serve_paths.get(self.next_serve_path)

        if path_data:

            for widget in self.root.children:
                if isinstance(widget, Image) and widget.source in path_data:
                    data = path_data[widget.source]
                    self.move_image_to_coordinates(widget, data['coordinates'], data['speed'])


            self.next_serve_path += 1


            if self.next_serve_path > len(serve_paths):
                self.next_serve_path = 1
        else:
            print("Nenhum conjunto de caminhos encontrado para o próximo saque.")

    def on_attack_button_press(self, instance):

        attack_paths = {
            1: {#Ajeitado
                'bola.png': {'coordinates': [(286, 174), (174, 288)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(353, 153), (295, 160)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(253, 162)], 'speed': 3},
                'timeA/Aponteiro1.png': {'coordinates': [(256, 196)], 'speed': 3},
                'timeA/Acentral.png': {'coordinates': [(137, 137)], 'speed': 3},
                'timeA/Aoposto.png': {'coordinates': [(194, 316)], 'speed': 3},
                'timeA/Alevantador.png': {'coordinates': [(40, 309)], 'speed': 3},

            },
            2: {#Ajeitado
                'bola.png': {'coordinates': [(259, 392), (348,402)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(241, 395)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(293, 374)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(293, 345)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(405, 400)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(355, 271)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(484, 246)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(400, 218)], 'speed': 2},
            },
            3: {#Ajeitado
                'bola.png': {'coordinates': [(350, 281),(272,276),(398,85)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(360, 282)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(249, 276)], 'speed': 3.8},
                'timeA/Aponteiro1.png': {'coordinates': [(249, 251)], 'speed': 3.8},
                'timeA/Alibero.png': {'coordinates': [(249, 309)], 'speed': 3.8},
                'timeA/Acentral.png': {'coordinates': [(58, 262)], 'speed': 3.8},
                'timeA/Aponteiro2.png': {'coordinates': [(204, 164)], 'speed': 3.8},
                'timeA/Alevantador.png': {'coordinates': [(207, 367)], 'speed': 3.8},

            },
            4: {  # Ajeitado
                'bola.png': {'coordinates': [(264, 175), (367,312)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(219,111),(249, 159)], 'speed': 3.8},
                'timeB/Boposto.png': {'coordinates': [(294, 188)], 'speed': 3.8},
                'timeB/Blibero.png': {'coordinates': [(294, 159)], 'speed': 3.8},
                'timeB/Bponteiro2.png': {'coordinates': [(317, 296)], 'speed': 3.8},

            },
        5:{
            'bola.png': {'coordinates': [(285, 144), (130, 148)], 'speed': 2},
            'timeB/Blibero.png': {'coordinates': [(335, 112), (304, 142)], 'speed': 3.8},
            'timeA/Aoposto.png': {'coordinates': [(257, 162)], 'speed': 3.8},
            'timeA/Alibero.png': {'coordinates': [(258, 201)], 'speed': 3.8},
            'timeA/Aponteiro2.png': {'coordinates': [(59, 283)], 'speed': 3.8},
            'timeA/Aponteiro1.png': {'coordinates': [(87, 145)], 'speed': 3.8},


        },
        6:{

        },

        }
        if self.next_attack_path == 6:
             self.next_attack_path = 1





        path_data = attack_paths.get(self.next_attack_path)

        if path_data:

            for widget in self.root.children:
                if isinstance(widget, Image) and widget.source in path_data:
                    data = path_data[widget.source]
                    self.move_image_to_coordinates(widget, data['coordinates'], data['speed'])


            self.next_attack_path += 1


            if self.next_attack_path > len(attack_paths):
                self.next_attack_path = 1
        else:
            pass

    def on_next_rotation_button_press(self, instance):
        rotation_paths = {
            1: {#Ajeitado
                'bola.png': {'coordinates': [(254, 439), (514, 443), (515, 390)], 'speed': 3},
                'timeB/Blevantador.png': {'coordinates': [(458, 284)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(422, 355),(530,391)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(416, 183)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(311, 184)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(307, 266)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(310, 356)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(131, 271)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(98, 184)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(113, 355)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(190, 378)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(240, 275)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(188, 165)], 'speed': 2},


            },
            2: {#Ajeitado
                'bola.png': {'coordinates': [(277, 450),(8,440),(21,157)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(133, 267)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(117, 354)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(210, 362)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(232, 276)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(189, 165)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(99, 182), (-1,159)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(434, 279)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(416, 366)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(420, 194)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(349, 156)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(309, 262)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(347, 376)], 'speed': 2},

            },
            3: {  # Ajeitado
                'bola.png': {'coordinates': [(512, 387)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(133, 267)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(117, 354)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(210, 362)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(232, 276)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(189, 165)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(92, 173)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(423, 192)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(440, 278)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(322, 184)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(314, 265)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(535, 384)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(309, 371)], 'speed': 2},

            },
            4:{
                'bola.png': {'coordinates': [(295, 440), (13, 437), (21,151)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(303, 274)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(334, 176)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(426, 356)], 'speed': 2},
                'timeB/Bponteiro1.png': {'coordinates': [(311, 368)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(2, 152)], 'speed': 2},

                'timeA/Aponteiro2.png': {'coordinates': [(135, 263)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(118, 355)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(213, 360)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(235, 274)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(228, 188)], 'speed': 2},

            },
            5:{
                'bola.png': {'coordinates': [(18, 159)], 'speed': 2},
                'timeA/Acentral.png': {'coordinates': [(-1, 157)], 'speed': 2},
                'timeA/Alevantador.png': {'coordinates': [(73, 265)], 'speed': 2},
                'timeA/Alibero.png': {'coordinates': [(113, 354)], 'speed': 2},
                'timeA/Aoposto.png': {'coordinates': [(233, 351)], 'speed': 2},
                'timeA/Aponteiro1.png': {'coordinates': [(235, 270)], 'speed': 2},
                'timeA/Aponteiro2.png': {'coordinates': [(212, 184)], 'speed': 2},

                'timeB/Bponteiro1.png': {'coordinates': [(309, 182)], 'speed': 2},
                'timeB/Bponteiro2.png': {'coordinates': [(423, 351)], 'speed': 2},
                'timeB/Bcentral.png': {'coordinates': [(314, 354)], 'speed': 2},
                'timeB/Blevantador.png': {'coordinates': [(307,267)], 'speed': 2},
                'timeB/Blibero.png': {'coordinates': [(458, 279)], 'speed': 2},
                'timeB/Boposto.png': {'coordinates': [(419, 183)], 'speed': 2},

            },
            6:{

            },


        }
        if self.next_rotation_path == 6:
             self.next_rotation_path = 1

        path_data = rotation_paths.get(self.next_rotation_path)

        if path_data:

            for widget in self.root.children:
                if isinstance(widget, Image) and widget.source in path_data:
                    data = path_data[widget.source]
                    self.move_image_to_coordinates(widget, data['coordinates'], data['speed'])


            self.next_rotation_path += 1

            if self.next_rotation_path > len(rotation_paths):
                self.next_rotation_path = 1
        else:
            print("Fim")

    def move_ball_to_next_coordinate(self):
        if not hasattr(self, 'serve_coordinates') or len(self.serve_coordinates) == 0:
            return

        next_coordinate = self.serve_coordinates.pop(0)


        animation = Animation(pos=next_coordinate, duration=0.2)
        animation.start(self.ball_image)

    def on_touch_down(self, instance, touch):
        print(f"Coordenadas x: {touch.x-47}, y: {touch.y-52}")

    def move_image_to_coordinates(self, image_widget, coordinates_list, speed):
        if not coordinates_list:
            return

        first_coordinate = coordinates_list.pop(0)
        Animation.cancel_all(image_widget)

        distance = abs(image_widget.pos[0] - first_coordinate[0]) + abs(image_widget.pos[1] - first_coordinate[1])
        duration = distance / (100 * speed)

        animation = Animation(pos=first_coordinate, duration=duration)

        if coordinates_list:
            animation.bind(on_complete=lambda instance, image=image_widget, coord_list=coordinates_list, spd=speed: self.move_image_to_coordinates(image, coord_list, spd))

        animation.start(image_widget)

if __name__ == '__main__':
    MyApp().run()
