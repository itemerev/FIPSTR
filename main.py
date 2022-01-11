from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        boxlayout = BoxLayout(orientation="vertical")

        button_trademarks = Button(
            text="Товарные знаки",
            on_press=self._on_press_tm
        )

        button_patents = Button(
            text="Патенты",
            on_press=self._on_press_pat
        )

        button_nmpt = Button(
            text='ГУ, НМПТ, ПрЭВМ, Базы данных',
            halign='center',
            text_size=(500, 20),
            on_press=self._on_press_nmpt
        )

        boxlayout.add_widget(button_trademarks)
        boxlayout.add_widget(button_patents)
        boxlayout.add_widget(button_nmpt)
        self.add_widget(boxlayout)

    def _on_press_tm(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'all_trademarks'

    def _on_press_pat(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'patents'

    def _on_press_nmpt(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'nmpt'


class AllTrademarks(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Основные кнопки
        boxlayout = BoxLayout(orientation="vertical")
        button_trademarks = Button(
            text="Товарные знаки",
            on_press=self._on_press_tm
        )
        button_well_known_trademarks = Button(
            text="Общеизвестные товарные знаки",
        )
        button_international_registrations = Button(
            text="Международные регистрации",
        )

        # Навигационные кнопки
        navigation = BoxLayout(size_hint=(1, 0.2))
        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        boxlayout.add_widget(button_trademarks)
        boxlayout.add_widget(button_well_known_trademarks)
        boxlayout.add_widget(button_international_registrations)
        boxlayout.add_widget(navigation)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        self.add_widget(boxlayout)

    def _on_press_tm(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'trademarks'

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class Patents(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical")
        button_inventions = Button(
            text="Изобретения",
            on_press=self._on_press_inventions
        )
        button_utility_models = Button(
            text="Полезные модели",
        )
        button_industrial_designs = Button(
            text="Промышленные образцы",
        )

        navigation = BoxLayout(size_hint=(1, 0.2))
        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        boxlayout.add_widget(button_inventions)
        boxlayout.add_widget(button_utility_models)
        boxlayout.add_widget(button_industrial_designs)
        boxlayout.add_widget(navigation)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        self.add_widget(boxlayout)

    def _on_press_inventions(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'inventions'

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class NMPT(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical")
        button_nmpt = Button(
            text="НИПТ и ГУ",
        )
        button_programs = Button(
            text="Программы",
        )
        button_data = Button(
            text="Базы данных",
        )
        button_tims = Button(
            text="Топологии интергральных микросхем",
        )

        navigation = BoxLayout(size_hint=(1, 0.27))
        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        boxlayout.add_widget(button_nmpt)
        boxlayout.add_widget(button_programs)
        boxlayout.add_widget(button_data)
        boxlayout.add_widget(button_tims)
        boxlayout.add_widget(navigation)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        self.add_widget(boxlayout)

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class Trademarks(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical")

        button_evidence = Button(
            text="Свидетельства",
            on_press=self._on_press_evidence
        )

        button_applications = Button(
            text="Заявки",
            on_press=self._on_press_applications
        )

        navigation = BoxLayout(size_hint=(1, 0.132))

        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        boxlayout.add_widget(button_evidence)
        boxlayout.add_widget(button_applications)
        boxlayout.add_widget(navigation)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        self.add_widget(boxlayout)

    def _on_press_evidence(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'find_screen'
        FindScreen.argument = 'tm'

    def _on_press_applications(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'find_screen'
        FindScreen.argument = 'tm_app'

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'all_trademarks'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class Inventions(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical")

        button_evidence = Button(
            text="Патенты",
            on_press=self._on_press_evidence
        )

        button_applications = Button(
            text="Заявки",
            on_press=self._on_press_applications
        )

        navigation = BoxLayout(size_hint=(1, 0.132))

        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        boxlayout.add_widget(button_evidence)
        boxlayout.add_widget(button_applications)
        boxlayout.add_widget(navigation)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        self.add_widget(boxlayout)

    def _on_press_evidence(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'find_screen'
        FindScreen.argument = 'inv'

    def _on_press_applications(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'find_screen'
        FindScreen.argument = 'inv_app'

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'patents'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class FindScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        argument = None
        parent_box = BoxLayout(
            orientation='vertical'
        )
        floatlayout = FloatLayout()
        boxlayout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        button_find = Button(
            text='Найти',
            on_press=self._on_press_find
        )

        text_input = TextInput(
            multiline=False,
        )

        # Навигационные кнопки
        navigation = BoxLayout(size_hint=(1, 0.065))
        button_back = Button(
            text="Назад",
            on_press=self._on_press_back
        )
        button_home = Button(
            text="Домой",
            on_press=self._on_press_home
        )

        floatlayout.add_widget(boxlayout)
        boxlayout.add_widget(text_input)
        boxlayout.add_widget(button_find)
        navigation.add_widget(button_back)
        navigation.add_widget(button_home)
        parent_box.add_widget(floatlayout)
        parent_box.add_widget(navigation)
        self.add_widget(parent_box)

    def _on_press_find(self, item, *args):
        item = FindScreen.argument

    def _on_press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'trademarks'

    def _on_press_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_window'


class NewApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main_window'))
        sm.add_widget(Trademarks(name='trademarks'))
        sm.add_widget(AllTrademarks(name='all_trademarks'))
        sm.add_widget(Patents(name='patents'))
        sm.add_widget(NMPT(name='nmpt'))
        sm.add_widget(Inventions(name='inventions'))
        sm.add_widget(FindScreen(name='find_screen'))

        return sm


if __name__ == '__main__':
    app = NewApp()
    app.run()
