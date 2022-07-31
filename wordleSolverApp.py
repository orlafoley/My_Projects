# Calculator through Kivy example: https://realpython.com/mobile-app-kivy-python/

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class WordleSolver(App):
    def build(self):
        # Create basic layout for the boxes
        main_layout = BoxLayout(orientation="vertical")
        green_label = Label(text="Enter your green letters in the correct place: ")
        green_boxes = BoxLayout(orientation='horizontal', padding=10, size_hint_y=None, height=100)
        yellow_label = Label(text="Enter your yellow letters in the correct place: ")
        yellow_boxes = BoxLayout(orientation='horizontal', padding=10, size_hint_y=None, height=100)
        grey_label = Label(text="Enter all grey letters: ")
        grey_box = BoxLayout(orientation='horizontal', padding=10, size_hint_y=None, height=100)
        self.submit = Button(text='Submit', background_color=get_color_from_hex('#787c7f'), on_press=self.filter_words)
        self.solutions = TextInput(background_color=get_color_from_hex('#787c7f'),
                                   readonly=True, halign="left", font_size=50,
                                   foreground_color=get_color_from_hex('#FFFFFF'))
        self.valid_words = ''

        # Add items to the layout
        main_layout.add_widget(green_label)
        main_layout.add_widget(green_boxes)
        main_layout.add_widget(yellow_label)
        main_layout.add_widget(yellow_boxes)
        main_layout.add_widget(grey_label)
        main_layout.add_widget(grey_box)
        main_layout.add_widget(self.submit)
        main_layout.add_widget(self.solutions)

        # Add the text boxes to input the right letters
        self.green_letters0 = TextInput(text="", background_color=get_color_from_hex('#6ca965'),
                                        font_size=50, halign='center')
        self.green_letters1 = TextInput(text="", background_color=get_color_from_hex('#6ca965'),
                                        font_size=50, halign='center')
        self.green_letters2 = TextInput(text="", background_color=get_color_from_hex('#6ca965'),
                                        font_size=50, halign='center')
        self.green_letters3 = TextInput(text="", background_color=get_color_from_hex('#6ca965'),
                                        font_size=50, halign='center')
        self.green_letters4 = TextInput(text="", background_color=get_color_from_hex('#6ca965'),
                                        font_size=50, halign='center')
        green_boxes.add_widget(self.green_letters0)
        green_boxes.add_widget(self.green_letters1)
        green_boxes.add_widget(self.green_letters2)
        green_boxes.add_widget(self.green_letters3)
        green_boxes.add_widget(self.green_letters4)
        self.yellow_letters0 = TextInput(text="", background_color=get_color_from_hex('#c8b653'),
                                         font_size=50, halign='center')
        self.yellow_letters1 = TextInput(text="", background_color=get_color_from_hex('#c8b653'),
                                         font_size=50, halign='center')
        self.yellow_letters2 = TextInput(text="", background_color=get_color_from_hex('#c8b653'),
                                         font_size=50, halign='center')
        self.yellow_letters3 = TextInput(text="", background_color=get_color_from_hex('#c8b653'),
                                         font_size=50, halign='center')
        self.yellow_letters4 = TextInput(text="", background_color=get_color_from_hex('#c8b653'),
                                         font_size=50, halign='center')
        yellow_boxes.add_widget(self.yellow_letters0)
        yellow_boxes.add_widget(self.yellow_letters1)
        yellow_boxes.add_widget(self.yellow_letters2)
        yellow_boxes.add_widget(self.yellow_letters3)
        yellow_boxes.add_widget(self.yellow_letters4)
        self.grey_letters = TextInput(text="", background_color=get_color_from_hex('#787c7f'),
                                      font_size=50, halign='center')
        grey_box.add_widget(self.grey_letters)

        # Displays the app
        return main_layout

    @staticmethod
    def wordleList(filename):
        """
        :param filename: text file of Wordle words
        :return: List of five-letter words
        """

        filein = open(filename, 'r')
        words = filein.readlines()
        dictionary = []

        for word in words:
            word = word.strip('\n').split('\t')
            dictionary += word

        filein.close()

        return dictionary

    @staticmethod
    def removeWord(words, letter):
        """
        Removes words from the list if they contain a grey letter
        """
        return [word for word in words if letter not in word]

    @staticmethod
    def keepWord(words, letter):
        """
        Keeps words in the list if they contain a letter
        """
        return [word for word in words if letter in word]

    @staticmethod
    def yellowWord(words, letter, place):
        """
        Keeps words in the list if they contain a letter not in a place
        """
        return [word for word in words if letter not in word[place]]

    @staticmethod
    def greenWord(words, letter, place):
        """
        Keeps words in the list if they contain a green letter
        """
        return [word for word in words if letter in word[place]]

    def filter_words(self, instance):
        # Collect all valid/invalid letters
        grey_letters = self.grey_letters.text
        yellow_letters = [self.yellow_letters0.text, self.yellow_letters1.text, self.yellow_letters2.text,
                          self.yellow_letters3.text, self.yellow_letters4.text]
        green_letters = [self.green_letters0.text, self.green_letters1.text, self.green_letters2.text,
                         self.green_letters3.text, self.green_letters4.text]

        # Use static functions
        wordList = self.wordleList('valid-wordle-words.txt')
        for letter in grey_letters:
            wordList = self.removeWord(wordList, letter.lower())
        for index, letter in enumerate(green_letters):
            wordList = self.greenWord(wordList, letter.lower(), index)
        for index, letter in enumerate(yellow_letters):
            if letter != '':
                wordList = self.keepWord(wordList, letter.lower())
                wordList = self.yellowWord(wordList, letter.lower(), index)
        self.valid_words = ' '.join(wordList)
        self.solutions.text = self.valid_words


if __name__ == "__main__":
    app = WordleSolver()
    app.title = 'Wordle Solver'
    app.run()
