"""
Reusable styled objects for Manim videos.
These maintain a consistent design language across all scenes.
"""

from manim import *


# Design system colors
PRIMARY_COLOR = "#3498db"  # Blue
SECONDARY_COLOR = "#e74c3c"  # Red
ACCENT_COLOR = "#f39c12"  # Orange
BACKGROUND_COLOR = "#2c3e50"  # Dark blue-gray
TEXT_COLOR = "#ecf0f1"  # Light gray


class StyledTitle(Text):
    """
    A styled title with consistent formatting.
    
    Usage:
        title = StyledTitle("My Video Title")
    """
    def __init__(self, text, **kwargs):
        super().__init__(
            text,
            font_size=72,
            color=TEXT_COLOR,
            weight=BOLD,
            **kwargs
        )


class StyledSubtitle(Text):
    """
    A styled subtitle with consistent formatting.
    
    Usage:
        subtitle = StyledSubtitle("Episode 1")
    """
    def __init__(self, text, **kwargs):
        super().__init__(
            text,
            font_size=36,
            color=ACCENT_COLOR,
            weight=NORMAL,
            **kwargs
        )


class StyledText(Text):
    """
    Standard body text with consistent formatting.
    
    Usage:
        text = StyledText("Some description")
    """
    def __init__(self, text, **kwargs):
        super().__init__(
            text,
            font_size=28,
            color=TEXT_COLOR,
            **kwargs
        )


class TitleCard(VGroup):
    """
    A complete title card with title, subtitle, and optional decorative elements.
    
    Usage:
        card = TitleCard("My Video", "Part 1")
    """
    def __init__(self, title_text, subtitle_text=None, **kwargs):
        self.title = StyledTitle(title_text)
        
        if subtitle_text:
            self.subtitle = StyledSubtitle(subtitle_text)
            self.subtitle.next_to(self.title, DOWN, buff=0.5)
            
            # Add decorative line between title and subtitle
            self.line = Line(
                start=LEFT * 3,
                end=RIGHT * 3,
                color=ACCENT_COLOR,
                stroke_width=3
            )
            self.line.next_to(self.title, DOWN, buff=0.2)
            
            super().__init__(self.title, self.line, self.subtitle, **kwargs)
        else:
            super().__init__(self.title, **kwargs)


class AccentBox(Rectangle):
    """
    A styled box for highlighting content.
    
    Usage:
        box = AccentBox(width=6, height=4)
    """
    def __init__(self, **kwargs):
        super().__init__(
            color=PRIMARY_COLOR,
            stroke_width=3,
            fill_opacity=0.1,
            **kwargs
        )


class StyledBulletPoint(VGroup):
    """
    A bullet point with consistent styling.
    
    Usage:
        bullet = StyledBulletPoint("First point")
    """
    def __init__(self, text, **kwargs):
        self.bullet = Dot(color=ACCENT_COLOR, radius=0.08)
        self.text = StyledText(text)
        self.text.next_to(self.bullet, RIGHT, buff=0.3)
        
        super().__init__(self.bullet, self.text, **kwargs)


def create_logo(scale=1.0, logo_path="./assets/website_logo.svg"):
    """
    Load and return the actual logo from SVG file.
    
    Args:
        scale: Size multiplier for the logo
        logo_path: Path to the SVG logo file (relative to the scene file)
                   Default: "../assets/website_logo.svg"
                   You can also use an absolute path if needed
    
    Returns:
        SVGMobject of the logo
    
    Usage:
        logo = create_logo(scale=0.8)
        # Or with custom path:
        logo = create_logo(scale=0.8, logo_path="/path/to/logo.svg")
    """
    try:
        logo = SVGMobject(logo_path)
        logo.scale(scale)
        return logo
    except Exception as e:
        # Fallback to placeholder if SVG can't be loaded
        print(f"Warning: Could not load logo from {logo_path}: {e}")
        print("Using placeholder logo instead.")
        circle = Circle(radius=0.5 * scale, color=PRIMARY_COLOR, fill_opacity=0.3)
        text = Text("LOGO", font_size=36 * scale, color=TEXT_COLOR)
        placeholder = VGroup(circle, text)
        return placeholder


def create_section_header(title, underline=True):
    """
    Create a styled section header.
    
    Args:
        title: The header text
        underline: Whether to add an underline
    
    Returns:
        VGroup containing the header elements
    """
    header = StyledTitle(title)
    header.scale(0.6)
    
    if underline:
        line = Line(
            start=header.get_left(),
            end=header.get_right(),
            color=ACCENT_COLOR,
            stroke_width=2
        )
        line.next_to(header, DOWN, buff=0.1)
        return VGroup(header, line)
    
    return VGroup(header)