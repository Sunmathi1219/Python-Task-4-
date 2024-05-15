


#Base TV class
class TV:
    def __init__(self,brand):
        self.brand=brand
        self.channel=1
        self.volume=50
        self.On=False
        self.price=30000
        

    def increase_volume(self):
        if self.volume<100:
            self.volume+=1

    def decrease_volume(self):
        if self.volume>0:
            self.volume-=1   

    def set_channel(self,current_channel):
         if 1<=current_channel<=50:
              self.current_channel=current_channel 

    def reset_channel(self):
            self.channel=1
            self.volume=50
            

    def status(self):
         return f"{self.brand} at channel {self.channel},volume {self.volume}"         

#LED TV
class LED_TV(TV):
     def __init__(self,brand,screen_thickness,energy_usage,life_span,refresh_rate):
          super().__init__(brand)
          self.screen_thickness=screen_thickness
          self.energy_usage=energy_usage
          self.life_span=life_span
          self.refresh_rate=refresh_rate

     def viewing_angle(self):
          self.viewing_angle=45

     def Back_light(self):
          self.Back_light="lighter"         
     

     def Display_details(self):    
          return f"Screen Thickness : {self.screen_thickness} inches \n Energy Usage : {self.energy_usage}W \n Life Span:{self.life_span} years \n Refresh rate : {self.refresh_rate}HZ \n Viewing angle : {self.viewing_angle} \n Back Light : {self.Back_light}" 
Led_Tv =LED_TV("Panasonic",1.8,50,6,70)
Led_Tv.set_channel(8)  
Led_Tv.increase_volume()
Led_Tv.viewing_angle()
Led_Tv.Back_light()
print(Led_Tv.status())
print(Led_Tv.Display_details())    

# Plasma Tv   
class Plasma_TV(TV):
     def __init__(self,brand,screen_thickness,energy_usage,life_span,refresh_rate):
          super().__init__(brand)
          self.screen_thickness=screen_thickness
          self.energy_usage=energy_usage
          self.life_span=life_span
          self.refresh_rate=refresh_rate

     def viewing_angle(self):
          self.viewing_angle=30

     def Back_light(self):
          self.Back_light=None         

     def Display_details(self):    
          return f"Screen Thickness : {self.screen_thickness} inches \n Energy Usage : {self.energy_usage}W \n Life Span:{self.life_span} years \n Refresh rate : {self.refresh_rate}HZ \n Viewing angle : {self.viewing_angle} \n Back Light : {self.Back_light}" 
     
plasma_tv=Plasma_TV("Redmi",2.3,120,8,40)
plasma_tv.set_channel(3)
plasma_tv.decrease_volume()
plasma_tv.reset_channel()
plasma_tv.viewing_angle()
plasma_tv.Back_light()
print(plasma_tv.status())
print(plasma_tv.Display_details())


            