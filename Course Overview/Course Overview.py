from manim import *
config.background_color = "#151515"

class Blank(Scene):
  def construct(self):
    self.wait()
    
class course(Scene):
   def construct(self):
      java = SVGMobject("Media/drawing-2.svg").scale(3).move_to(RIGHT*3.8).shift(DOWN*0.3)
      learn = Text("LEARN JAVA", font="Chivo", weight="ULTRAHEAVY").next_to(java, LEFT).scale(1.5).shift(UP*0.3)
      title = Text("Course Overview", font="Noto Sans Mono").next_to(learn, DOWN*0.5).scale(0.45)
      
      self.add(java)
      self.add(learn)
      self.add(title)
      self.wait()
      
class JAVAintro(Scene):
   def construct(self):
      java = SVGMobject("Media/Java_(programming_language)-Logo.wine.svg").scale(3)
      james = ImageMobject("Media/jamesgosling1642web.jpg").scale(0.4).shift(RIGHT*3).set_opacity(0.8)
      android = SVGMobject("Media/android.svg").scale(3)
      
      self.play(DrawBorderThenFill(java), run_time=2)
      self.wait(0.5)
      self.play(java.animate.shift(LEFT*3.2), run_time=0.8)
      self.add(james)
      self.play(FadeIn(james))
      self.wait(3)
      
class android(Scene):
   def construct(self):
      android = SVGMobject("Media/android.svg").scale(3)
      
      self.play(GrowFromCenter(android), runtime=0.2, rate_func=rate_functions.ease_out_sine)
      self.wait(2)
      
class eshaan(Scene):
   def construct(self):
      thi = Text("this is ", font="Cascadia Code").move_to(LEFT*2)
      thi2 = Text("this is:", font="Cascadia Code", color="#ff006a", weight="LIGHT").move_to(LEFT*2)
      esh = Text(" nveshaan_", font="Cascadia Code").next_to(thi, RIGHT).shift(DOWN*0.07)
      esh2 = Text(" nveshaan;", font="Cascadia Code", color="#70d622", weight="LIGHT").next_to(thi, RIGHT).shift(DOWN*0.03)
      cmd = Text(">_", font="Cascadia Code", weight="HEAVY").shift(RIGHT*5.75 + UP*3).scale(0.8)
      framebox1 = RoundedRectangle(corner_radius=0.2, width=13.0, height=7.0)
      dot1 = Dot(color=RED).shift(LEFT*6 + UP*3).scale(1.5)
      dot2 = Dot(color=YELLOW).shift(LEFT*5.5 + UP*3).scale(1.5)
      dot3 = Dot(color=GREEN).shift(LEFT*5 + UP*3).scale(1.5)
      
      self.add(thi)
      self.add(esh)
      self.add(cmd)
      self.add(framebox1)
      self.add(dot1)
      self.add(dot2)
      self.add(dot3)
      self.wait(1.5)
      self.play(Transform(thi, thi2), run_time=0.7)
      self.play(Transform(esh, esh2), run_time=0.7)
      self.wait()
      
class course(Scene):
   def construct(self):
      java = SVGMobject("Media/drawing-2.svg").scale(3).move_to(RIGHT*3.8).shift(DOWN*0.3)
      learn = Text("LEARN JAVA", font="Chivo", weight="ULTRAHEAVY").next_to(java, LEFT).scale(1.5)

      self.play(SpinInFromNothing(java))
      self.wait()
      self.play(Write(learn))
      self.wait()

class icse(Scene):
   def construct(self):
      icse = ImageMobject("Media/Picture2.png").scale(3)

      self.play(FadeIn(icse))
      self.wait(6)
      
class github(Scene):
   def construct(self):
      git = ImageMobject("Media/Picture1.png")
      box = RoundedRectangle(corner_radius=0.05, height=0.33, width=2.7, color="#1cbd1c").shift(UP*3.53, LEFT*4)

      self.add(git)
      self.wait(4)
      self.play(Create(box))
      self.wait(0.5)
      self.play(Wiggle(box))
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
     self.wait()
