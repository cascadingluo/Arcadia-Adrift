import pygame
import random
from scenes import global_data

class QuizScene:
    def __init__(self, player_pos):
        self.image = pygame.transform.scale(pygame.image.load(r"assets/images/oceanbg-noins.png").convert(), (1280, 800))
        self.player_pos = player_pos
        self.button_rect = pygame.Rect(1050, 30, 200, 80)
        all_questions = [
        {
            "question": "What is the primary impact of melting sea ice on Arctic animals like polar bears and walruses?",
            "options": [
                "It improves their access to warmer ocean currents for migration",
                "It makes it harder for them to find food and hunt",
                "It leads to overpopulation due to fewer natural predators",
                "It enhances their ability to communicate over long distances"
            ],
            "answer": 1
        },
        {
            "question": "What effect does climate change have on Arctic vegetation?",
            "options": [
                "More insects will appear",
                "Less crops will grow",
                "Climate change causes the tundra to become a lush rainforest",
                "Plant life increases dramatically, allowing for commercial agriculture"
            ],
            "answer": 1
        },
        {
            "question": "How will changes in the Arctic affect the whole planet?",
            "options": [
                "Global temperatures will stabilize due to polar cloud formation",
                "Changing Arctic wind patterns will lead to permanent jet stream collapse",
                "Ocean current will remain the same",
                "Food sources like fish will decrease"
            ],
            "answer": 3
        },
        {
            "question": "What is one major reason why the Arctic is warming faster than the rest of the planet?",
            "options": [
                "Melting sea ice reduces reflectivity, causing the ocean to absorb more heat",
                "Arctic vegetation is releasing methane at an accelerated rate",
                "Solar flares are concentrating on the Arctic due to Earth’s magnetic field shift",
                "Shipping traffic is directly heating the region’s atmosphere"
            ],
            "answer": 0
        },
        {
            "question": "What is a global consequence of the Greenland Ice Sheet melting?",
            "options": [
                "It will trigger tectonic activity in the Southern Hemisphere",
                "It will make the Arctic Ocean non-navigable due to increased salinity",
                "It will balance out Antarctic ice growth, stabilizing sea levels",
                "It will significantly contribute to sea level rise worldwide"
            ],
            "answer": 3
        },
        {
            "question": "Why is the loss of Arctic summer sea ice so concerning?",
            "options": [
                "It increases global humidity levels, leading to excess rainfall",
                "It reduces the planet’s oxygen supply by interfering with ocean currents",
                "It threatens ice-dependent species like narwhals, polar bears, and walruses",
                "It causes whales to migrate to freshwater ecosystems"
            ],
            "answer": 2
        },
        {
            "question": "What risk does thawing permafrost pose to Arctic communities?",
            "options": [
                "It releases underwater volcanoes trapped beneath the ice",
                "It alters cloud formation, leading to extended dry seasons",
                "It can destabilize infrastructure like buildings and pipelines",
                "It makes the soil too nutrient-rich, killing native plant species"
            ],
            "answer": 2
        },
        {
            "question": "Why are Arctic wildfires a serious climate concern?",
            "options": [
                "They improve soil fertility, increasing invasive plant spread",
                "They cause atmospheric thinning that accelerates UV radiation",
                "They release ancient viruses frozen in ice, spreading illness globally.",
                "They release greenhouse gases and destroy key habitats"
            ],
            "answer": 3
        },
        {
            "question": "How is coastal erosion affecting Arctic regions?",
            "options": [
                "It creates sinkholes that rapidly drain glacial lakes.",
                "It causes flooding, damages communities, and destroys cultural heritage.",
                "It shifts magnetic north further toward the equator.",
                "It increases whale strandings due to altered sonar paths."
            ],
            "answer": 1
        }
        ]   

        self.correct_this_session = 0

        random.shuffle(all_questions)
        self.questions = all_questions[:3]  # Select only 3 questions for this session

        random.shuffle(self.questions)
        self.current_question = 0
        self.selected = None
        self.feedback_timer = None
        self.wait_time = 1000
        self.finished = False

        self.font = pygame.font.SysFont("Arial", 28)
        self.title_font = pygame.font.SysFont("Arial", 36)
        self.correct_color = (167, 242, 217)
        self.incorrect_color = (250, 162, 200)
        self.option_rects = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.finished:
            if self.selected is None:
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(event.pos):
                        self.selected = i
                        self.feedback_timer = pygame.time.get_ticks()
            if self.button_rect.collidepoint(event.pos):
                from scenes.map import MapScene
                return MapScene(self.player_pos)  # just return to the map

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)  # add the last line
        return lines

    def update(self):
        if self.selected is not None:
            now = pygame.time.get_ticks()
            if now - self.feedback_timer > self.wait_time:
                q = self.questions[self.current_question]
                if self.selected == q["answer"]:
                    self.correct_this_session += 1
                    global_data.correct_answers_total += 1

                self.selected = None
                self.current_question += 1
                self.feedback_timer = None

                if self.current_question >= len(self.questions):
                    if global_data.correct_answers_total >= 3:
                        global_data.trivia_completed = True
                        from scenes.success import successful
                        return successful(self.player_pos)
                    else:
                        from scenes.unsuccess import unsuccessful
                        return unsuccessful(self.player_pos)
                    from scenes.map import MapScene
                    return MapScene(self.player_pos)

        return None


    def render(self, screen):
        screen.blit(self.image, (0,0))

        #button to exit out of trivia 
        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20)
        text = self.font.render("Back to Map", True, (0, 0, 0))
        button_rect = text.get_rect(center=self.button_rect.center)
        screen.blit(text, button_rect)

        if self.finished:
            text = self.title_font.render("Thanks for playing Arctic Trivia!", True, (0, 0, 0))
            screen.blit(text, text.get_rect(center=(640, 400)))
            return

        q = self.questions[self.current_question]
        wrapped_lines = self.wrap_text(q["question"], self.title_font, 1000)
        for i, line in enumerate(wrapped_lines):
            line_surf = self.title_font.render(line.strip(), True, (0, 0, 0))
            screen.blit(line_surf, (50, 50 + i * 40))

        self.option_rects = []
        for i, option in enumerate(q["options"]):
            rect = pygame.Rect(100, 150 + i * 80, 1080, 60)
            color = (225, 239, 246)
            if self.selected is not None:
                if i == q["answer"]:
                    color = self.correct_color
                elif i == self.selected:
                    color = self.incorrect_color

            pygame.draw.rect(screen, color, rect)
            text = self.font.render(option, True, (0, 0, 0))
            screen.blit(text, (rect.x + 10, rect.y + 15))
            self.option_rects.append(rect)

        pygame.display.flip()