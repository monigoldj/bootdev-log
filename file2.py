def overlaps(self, rect)
    if (
        self.get_left_x() <= rect.get_right_x()
        and self.get_right_x() >= rect.get_left_x()
        and self.get_top_y() >= rect.get_bottom_y()
        and self.get_bottom_y() <= rect.get_bottom_y()
    ):
        return True
    elif (
        rect.get_left_x() <= self.get_right_x()
        and rect.get_right_x() >= self.get_left_x()
        and rect.get_top_y() >= self.get_bottom_y()
        and rect.get_bottom_y() <= self.get_bottom_y()
    ):
        return True
    return False