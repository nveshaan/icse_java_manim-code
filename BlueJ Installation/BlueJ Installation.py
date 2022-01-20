from manim import *
config.background_color = "#151515"

class Blank(Scene):
  def construct(self):
    self.wait()
    
class thumbnail(Scene):
   def construct(self):
      java = SVGMobject("Media/drawing-2.svg").scale(3).move_to(RIGHT*3.8).shift(DOWN*0.3)
      learn = Text("LEARN JAVA", font="Chivo", weight="ULTRAHEAVY").next_to(java, LEFT).scale(1.5).shift(UP*0.3)
      title = Text("BlueJ Installation", font="Noto Sans Mono").next_to(learn, DOWN*0.5).scale(0.45)
      
      self.add(java)
      self.add(learn)
      self.add(title)
      self.wait()

class eshaan(Scene):
   def construct(self):
      thi = Text("this is ", font="Cascadia Code").move_to(LEFT*2)
      thi2 = Text("this is:", font="Cascadia Code", color="#ff006a", weight="LIGHT").move_to(LEFT*2)
      esh = Text(" nveshaan_", font="Cascadia Code").next_to(thi, RIGHT).shift(DOWN*0.07)
      esh2 = Text(" nveshaan;", font="Cascadia Code", color="#70d622", weight="LIGHT").next_to(thi, RIGHT).shift(DOWN*0.03)
      cmd = Text(">_", font="Cascadia Code", weight="HEAVY").shift(RIGHT*5.75 + UP*3).scale(0.8)
      window = RoundedRectangle(corner_radius=0.2, width=13.0, height=7.0)
      dot1 = Dot(color=RED).shift(LEFT*6 + UP*3).scale(1.5)
      dot2 = Dot(color=YELLOW).shift(LEFT*5.5 + UP*3).scale(1.5)
      dot3 = Dot(color=GREEN).shift(LEFT*5 + UP*3).scale(1.5)
      dots = VGroup(dot1, dot2, dot3)
      
      self.wait()
      self.play(Create(dots, run_time=1.2, rate_func=rate_functions.ease_out_quint), Create(window, run_time=1.5), Write(cmd, run_time=1.5), Write(thi2, run_time=1.5), Write(esh2, run_time=1.5))
      self.wait()

class intro(Scene):
   def construct(self):
      bluej = ImageMobject("Media/bluej-icon-png-5570.png").scale(2)
      win = ImageMobject("Media/11.png").shift(LEFT*3)
      win10 = ImageMobject("Media/10.png").scale(0.2).shift(RIGHT*3)
      win87 = ImageMobject("Media/8.png").scale(2).shift(RIGHT*3)

      self.play(FadeIn(bluej))
      self.wait()
      self.play(bluej.animate.shift(LEFT*3))
      self.wait(0.3)
      self.play(FadeIn(win10))
      self.wait()
      self.remove(bluej, win10)
      self.play(FadeIn(win), FadeIn(win87))
      self.wait(3)

class os(Scene):
   def construct(self):
      mac = ImageMobject("Media/mac.png").shift(LEFT*3).scale(0.9)
      ubuntu = ImageMobject("Media/ubuntu.png").shift(RIGHT*3).scale(0.4)

      self.play(FadeIn(mac))
      self.play(FadeIn(ubuntu))
      self.wait(4)

class outro(Scene):
   def construct(self):
     circle = Circle(radius=1.2, color="#151515").shift(LEFT*2)
     self.add(circle)
     self.play(Flash(
            circle, line_length=1,
            num_lines=20, color=WHITE,
            flash_radius=1.2+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
     self.play(Flash(
            circle, line_length=1,
            num_lines=20, color=WHITE,
            flash_radius=1.2+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
     self.play(Flash(
            circle, line_length=1,
            num_lines=20, color=WHITE,
            flash_radius=1.2+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
     self.wait()