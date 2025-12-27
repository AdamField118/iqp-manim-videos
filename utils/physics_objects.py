"""
Physics-specific utilities for gravity and mechanics animations.
These objects and functions are designed for the Universal Gravitation video series.
"""

from manim import *


def create_mass(label="m", radius=0.5, color=BLUE, show_label=True):
    """
    Create a labeled mass (circle) for physics demonstrations.
    
    Args:
        label: Text label for the mass (e.g., "m₁", "m₂", "M")
        radius: Size of the mass
        color: Color of the mass
        show_label: Whether to show the label
    
    Returns:
        VGroup containing the mass and its label
    """
    mass_circle = Circle(
        radius=radius,
        fill_color=color,
        fill_opacity=0.7,
        stroke_color=WHITE,
        stroke_width=2
    )
    
    if show_label:
        mass_label = MathTex(label, font_size=36, color=WHITE)
        mass_label.move_to(mass_circle.get_center())
        return VGroup(mass_circle, mass_label)
    else:
        return VGroup(mass_circle)


def create_earth(radius=1.5, show_continents=True):
    """
    Create a stylized Earth for physics demonstrations.
    
    Args:
        radius: Size of Earth
        show_continents: Whether to add continent-like decorations
    
    Returns:
        VGroup representing Earth
    """
    earth = Circle(
        radius=radius,
        fill_color=BLUE,
        fill_opacity=0.8,
        stroke_color=BLUE_E,
        stroke_width=3
    )
    
    if show_continents:
        # Add simple continent shapes
        continent1 = Ellipse(
            width=radius * 0.6,
            height=radius * 0.4,
            fill_color=GREEN,
            fill_opacity=0.6,
            stroke_width=0
        )
        continent1.shift(UP * radius * 0.3 + LEFT * radius * 0.2)
        
        continent2 = Ellipse(
            width=radius * 0.4,
            height=radius * 0.5,
            fill_color=GREEN,
            fill_opacity=0.6,
            stroke_width=0
        )
        continent2.shift(DOWN * radius * 0.2 + RIGHT * radius * 0.3)
        
        return VGroup(earth, continent1, continent2)
    else:
        return VGroup(earth)


def create_force_arrow(start_point, end_point, label="F", color=YELLOW, label_position=None):
    """
    Create a labeled force arrow.
    
    Args:
        start_point: Starting position of arrow
        end_point: Ending position of arrow
        label: Label for the force
        color: Color of the arrow
        label_position: Position for label (None = auto)
    
    Returns:
        VGroup containing arrow and label
    """
    arrow = Arrow(
        start=start_point,
        end=end_point,
        color=color,
        stroke_width=6,
        buff=0,
        max_tip_length_to_length_ratio=0.15
    )
    
    force_label = MathTex(label, font_size=32, color=color)
    
    if label_position is None:
        # Auto-position label near arrow midpoint
        midpoint = (np.array(start_point) + np.array(end_point)) / 2
        direction = np.array(end_point) - np.array(start_point)
        perpendicular = np.array([-direction[1], direction[0], 0])
        perpendicular = perpendicular / np.linalg.norm(perpendicular) if np.linalg.norm(perpendicular) > 0 else perpendicular
        force_label.move_to(midpoint + perpendicular * 0.4)
    else:
        force_label.move_to(label_position)
    
    return VGroup(arrow, force_label)


def create_attraction_arrows(obj1, obj2, color=YELLOW, label1="F", label2="F"):
    """
    Create bidirectional attraction arrows between two objects.
    (Old style - arrows go from edge to edge)
    
    Args:
        obj1: First object
        obj2: Second object
        color: Color of arrows
        label1: Label for force on object 1
        label2: Label for force on object 2
    
    Returns:
        VGroup containing both arrows
    """
    center1 = obj1.get_center()
    center2 = obj2.get_center()
    
    # Calculate edge points for arrows
    direction = center2 - center1
    distance = np.linalg.norm(direction)
    unit_direction = direction / distance if distance > 0 else direction
    
    # Start arrows from object edges
    radius1 = max(obj1.width, obj1.height) / 2
    radius2 = max(obj2.width, obj2.height) / 2
    
    start1 = center1 + unit_direction * radius1
    end1 = center2 - unit_direction * radius2
    
    start2 = center2 - unit_direction * radius2
    end2 = center1 + unit_direction * radius1
    
    arrow1 = Arrow(start1, end1, color=color, stroke_width=4, buff=0)
    arrow2 = Arrow(start2, end2, color=color, stroke_width=4, buff=0)
    
    return VGroup(arrow1, arrow2)


def create_fbd_force_arrows(obj1, obj2, arrow_length=1.0, color=YELLOW, stroke_width=4):
    """
    Create free body diagram style force arrows - fixed length arrows pointing 
    from the center of each object toward the other object.
    
    Args:
        obj1: First object
        obj2: Second object  
        arrow_length: Length of each arrow (in Manim units)
        color: Color of arrows
        stroke_width: Thickness of arrows
    
    Returns:
        VGroup containing both arrows (one from each object's center)
    """
    center1 = obj1.get_center()
    center2 = obj2.get_center()
    
    # Calculate direction from obj1 to obj2
    direction_1_to_2 = center2 - center1
    distance = np.linalg.norm(direction_1_to_2)
    unit_direction_1_to_2 = direction_1_to_2 / distance if distance > 0 else direction_1_to_2
    
    # Direction from obj2 to obj1 is opposite
    unit_direction_2_to_1 = -unit_direction_1_to_2
    
    # Create arrow from center of obj1 pointing toward obj2
    arrow1_start = center1
    arrow1_end = center1 + unit_direction_1_to_2 * arrow_length
    arrow1 = Arrow(
        arrow1_start, 
        arrow1_end, 
        color=color, 
        stroke_width=stroke_width, 
        buff=0,
        max_tip_length_to_length_ratio=0.25
    )
    
    # Create arrow from center of obj2 pointing toward obj1
    arrow2_start = center2
    arrow2_end = center2 + unit_direction_2_to_1 * arrow_length
    arrow2 = Arrow(
        arrow2_start, 
        arrow2_end, 
        color=color, 
        stroke_width=stroke_width, 
        buff=0,
        max_tip_length_to_length_ratio=0.25
    )
    
    return VGroup(arrow1, arrow2)


def create_simple_person(height=1.0, color=WHITE):
    """
    Create a simple stick figure person.
    
    Args:
        height: Height of the person
        color: Color of the stick figure
    
    Returns:
        VGroup representing a person
    """
    head = Circle(radius=height * 0.15, color=color, fill_opacity=0.5)
    head.shift(UP * height * 0.35)
    
    body = Line(
        start=head.get_bottom(),
        end=head.get_bottom() + DOWN * height * 0.4,
        color=color,
        stroke_width=3
    )
    
    # Arms
    arm_height = head.get_bottom() + DOWN * height * 0.15
    left_arm = Line(
        start=arm_height,
        end=arm_height + LEFT * height * 0.25 + DOWN * height * 0.1,
        color=color,
        stroke_width=3
    )
    right_arm = Line(
        start=arm_height,
        end=arm_height + RIGHT * height * 0.25 + DOWN * height * 0.1,
        color=color,
        stroke_width=3
    )
    
    # Legs
    leg_top = body.get_bottom()
    left_leg = Line(
        start=leg_top,
        end=leg_top + LEFT * height * 0.15 + DOWN * height * 0.35,
        color=color,
        stroke_width=3
    )
    right_leg = Line(
        start=leg_top,
        end=leg_top + RIGHT * height * 0.15 + DOWN * height * 0.35,
        color=color,
        stroke_width=3
    )
    
    return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)


def create_phone(scale=1.0, color=GREY):
    """
    Create a simple phone icon.
    
    Args:
        scale: Size multiplier
        color: Color of the phone
    
    Returns:
        VGroup representing a phone
    """
    phone_body = Rectangle(
        width=0.4 * scale,
        height=0.7 * scale,
        fill_color=color,
        fill_opacity=0.8,
        stroke_color=WHITE,
        stroke_width=2
    )
    
    screen = Rectangle(
        width=0.32 * scale,
        height=0.5 * scale,
        fill_color=BLUE_E,
        fill_opacity=0.5,
        stroke_width=0
    )
    screen.move_to(phone_body.get_center() + UP * 0.05 * scale)
    
    button = Circle(
        radius=0.05 * scale,
        fill_color=GREY,
        fill_opacity=0.5,
        stroke_width=1
    )
    button.move_to(phone_body.get_bottom() + UP * 0.1 * scale)
    
    return VGroup(phone_body, screen, button)


def create_desk(scale=1.0, color=GREY_BROWN):
    """
    Create a simple desk icon.
    
    Args:
        scale: Size multiplier
        color: Color of the desk
    
    Returns:
        VGroup representing a desk
    """
    top = Rectangle(
        width=1.5 * scale,
        height=0.15 * scale,
        fill_color=color,
        fill_opacity=0.8,
        stroke_color=WHITE,
        stroke_width=2
    )
    
    left_leg = Rectangle(
        width=0.1 * scale,
        height=0.6 * scale,
        fill_color=color,
        fill_opacity=0.8,
        stroke_width=0
    )
    left_leg.next_to(top, DOWN, buff=0)
    left_leg.shift(LEFT * 0.6 * scale)
    
    right_leg = Rectangle(
        width=0.1 * scale,
        height=0.6 * scale,
        fill_color=color,
        fill_opacity=0.8,
        stroke_width=0
    )
    right_leg.next_to(top, DOWN, buff=0)
    right_leg.shift(RIGHT * 0.6 * scale)
    
    return VGroup(top, left_leg, right_leg)


def create_ball(radius=0.3, color=RED, pattern=True):
    """
    Create a simple ball.
    
    Args:
        radius: Size of the ball
        color: Color of the ball
        pattern: Whether to add a pattern/shading
    
    Returns:
        VGroup representing a ball
    """
    ball = Circle(
        radius=radius,
        fill_color=color,
        fill_opacity=0.8,
        stroke_color=WHITE,
        stroke_width=2
    )
    
    if pattern:
        # Add a highlight
        highlight = Circle(
            radius=radius * 0.3,
            fill_color=WHITE,
            fill_opacity=0.3,
            stroke_width=0
        )
        highlight.shift(UP * radius * 0.3 + LEFT * radius * 0.3)
        return VGroup(ball, highlight)
    else:
        return VGroup(ball)