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
                "answer": 1,
                "explanation": "Melting sea ice removes hunting platforms, making it harder for them to find food."
            },
            {
                "question": "What effect does climate change have on Arctic vegetation?",
                "options": [
                    "More insects will appear",
                    "Less crops will grow",
                    "Climate change causes the tundra to become a lush rainforest",
                    "Plant life increases dramatically, allowing for commercial agriculture"
                ],
                "answer": 0,
                "explanation": "Warming allows more insects to survive and spread in the Arctic."
            },
            {
                "question": "How will changes in the Arctic affect the whole planet?",
                "options": [
                    "Global temperatures will stabilize due to polar cloud formation",
                    "Changing Arctic wind patterns will lead to permanent jet stream collapse",
                    "Ocean current will remain the same",
                    "Food sources like fish will decrease"
                ],
                "answer": 3,
                "explanation": "Arctic changes disrupt global fish stocks, impacting food sources worldwide."
            },
            {
                "question": "What is one major reason why the Arctic is warming faster than the rest of the planet?",
                "options": [
                    "Melting sea ice reduces reflectivity, causing the ocean to absorb more heat",
                    "Arctic vegetation is releasing methane at an accelerated rate",
                    "Solar flares are concentrating on the Arctic due to Earth’s magnetic field shift",
                    "Shipping traffic is directly heating the region’s atmosphere"
                ],
                "answer": 0,
                "explanation": "Melting sea ice exposes darker ocean water, which absorbs more heat (ice-albedo feedback)."
            },
            {
                "question": "What is a global consequence of the Greenland Ice Sheet melting?",
                "options": [
                    "It will trigger tectonic activity in the Southern Hemisphere",
                    "It will make the Arctic Ocean non-navigable due to increased salinity",
                    "It will balance out Antarctic ice growth, stabilizing sea levels",
                    "It will significantly contribute to sea level rise worldwide"
                ],
                "answer": 3,
                "explanation": "Melting the Greenland Ice Sheet raises sea levels globally."
            },
            {
                "question": "Why is the loss of Arctic summer sea ice so concerning?",
                "options": [
                    "It increases global humidity levels, leading to excess rainfall",
                    "It reduces the planet’s oxygen supply by interfering with ocean currents",
                    "It threatens ice-dependent species like narwhals, polar bears, and walruses",
                    "It causes whales to migrate to freshwater ecosystems"
                ],
                "answer": 2,
                "explanation": "Losing sea ice endangers species like polar bears that depend on it."
            },
            {
                "question": "What risk does thawing permafrost pose to Arctic communities?",
                "options": [
                    "It releases underwater volcanoes trapped beneath the ice",
                    "It alters cloud formation, leading to extended dry seasons",
                    "It can destabilize infrastructure like buildings and pipelines",
                    "It makes the soil too nutrient-rich, killing native plant species"
                ],
                "answer": 2,
                "explanation": "Thawing permafrost destabilizes the ground, damaging infrastructure."
            },
            {
                "question": "Why are Arctic wildfires a serious climate concern?",
                "options": [
                    "They improve soil fertility, increasing invasive plant spread",
                    "They cause atmospheric thinning that accelerates UV radiation",
                    "They release ancient viruses frozen in ice, spreading illness globally.",
                    "They release greenhouse gases and destroy key habitats"
                ],
                "answer": 3,
                "explanation": "Arctic wildfires release greenhouse gases and destroy ecosystems."
            },
            {
                "question": "How is coastal erosion affecting Arctic regions?",
                "options": [
                    "It creates sinkholes that rapidly drain glacial lakes.",
                    "It causes flooding, damages communities, and destroys cultural heritage.",
                    "It shifts magnetic north further toward the equator.",
                    "It increases whale strandings due to altered sonar paths."
                ],
                "answer": 1,
                "explanation": "Coastal erosion floods communities and damages cultural heritage."
            }
        ]

        self.correct_this_session = 0

        random.shuffle(all_questions)
        self.questions = all_questions[:3] # Select 3 random questions
        self.current_question = 0
        self.selected = None
        self.feedback_timer = None
        self.feedback_duration = 1000  # 1 second for correct
        self.explanation_duration = 3000  # 3 seconds for wrong
        self.waiting_for_explanation = False
        self.explanation_text = None

        self.font = pygame.font.SysFont("Arial", 28)
        self.title_font = pygame.font.SysFont("Arial", 36)
        self.correct_color = (167, 242, 217)
        self.incorrect_color = (250, 162, 200)
        self.option_rects = []

        self.finished = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.finished:
            if self.selected is None and not self.waiting_for_explanation:
                global_data.play_audio()
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(event.pos):
                        self.selected = i
                        q = self.questions[self.current_question]
                        if self.selected == q["answer"]:
                            self.feedback_timer = pygame.time.get_ticks()
                        else:
                            self.feedback_timer = pygame.time.get_ticks()
                            self.waiting_for_explanation = True
                            self.explanation_text = q["explanation"]

            if self.button_rect.collidepoint(event.pos):
                global_data.play_audio()
                from scenes.map import MapScene
                return MapScene(self.player_pos)

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
        lines.append(current_line)
        return lines

    def update(self):
        if self.selected is not None:
            now = pygame.time.get_ticks()
            if not self.waiting_for_explanation:
                if now - self.feedback_timer > self.feedback_duration:
                    q = self.questions[self.current_question]
                    if self.selected == q["answer"]:
                        self.correct_this_session += 1
                        global_data.correct_answers_total += 1
                    self.selected = None
                    self.current_question += 1
                    self.feedback_timer = None
            else:
                if now - self.feedback_timer > self.explanation_duration:
                    self.selected = None
                    self.waiting_for_explanation = False
                    self.explanation_text = None
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

        return None

    def render(self, screen):
        screen.blit(self.image, (0,0))

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

        if self.waiting_for_explanation and self.explanation_text:
            explanation_lines = self.wrap_text(self.explanation_text, self.font, 1000)
            y_offset = 650
            for line in explanation_lines:
                explanation_surf = self.font.render(line.strip(), True, (0, 0, 0))
                explanation_bg = pygame.Surface((explanation_surf.get_width() + 20, explanation_surf.get_height() + 10))
                explanation_bg.fill((255, 255, 200))
                screen.blit(explanation_bg, (50, y_offset))
                screen.blit(explanation_surf, (60, y_offset + 5))
                y_offset += 40
        
        juniper  = pygame.transform.scale(pygame.image.load(r"assets/images/juniper-portrait.png").convert(), (220, 295))
        screen.blit(juniper, (1040, 480))

        pygame.display.flip()
