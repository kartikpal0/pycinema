PRICES = {"Adult": 800, "Student": 600, "Child": 500}
STUDENT_DISCOUNT = 0.10   # 2 or more student tickets
GROUP_DISCOUNT = 0.05     # 5 or more tickets in total


def calculate(adult, student, child):
    adult_cost = adult * PRICES["Adult"]
    student_cost = student * PRICES["Student"]
    child_cost = child * PRICES["Child"]
    subtotal = adult_cost + student_cost + child_cost
    total = adult + student + child

    student_disc = student_cost * STUDENT_DISCOUNT if student >= 2 else 0
    after_student = subtotal - student_disc
    group_disc = after_student * GROUP_DISCOUNT if total >= 5 else 0

    return {
        "adult_cost": adult_cost,
        "student_cost": student_cost,
        "child_cost": child_cost,
        "subtotal": subtotal,
        "student_discount": student_disc,
        "after_student": after_student,
        "group_discount": group_disc,
        "final": round(after_student - group_disc, 2),
        "total_tickets": total,
    }
