from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class HelloWorldApp(App):
    def build(self):
        # Set window background color (optional)
        Window.clearcolor = (1, 1, 1, 1)
        
        # Create a layout
        layout = BoxLayout(orientation='vertical', padding=50)
        
        # Create a label with Hello World text
        label = Label(
            text='Hello World!',
            font_size='32sp',
            color=(0, 0, 0, 1),  # Black text
            bold=True
        )
        
        # Add label to layout
        layout.add_widget(label)
        
        return layout

if __name__ == '__main__':
    HelloWorldApp().run()