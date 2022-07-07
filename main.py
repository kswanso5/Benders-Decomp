"""
Main file
Solving the production problem with L-shaped method
"""

# import
from stochastic_programing import Two_Stage_Stochastic_Program


# main
def main():
    """
    main
    """
    # define problem
    production = Two_Stage_Stochastic_Program(
        name="production"
    )
    # build extensive form
    extensive = production.build_extensive_form()
    # solve entensive
    extensive.optimize()
    # solve two-stage
    production.L_shaped()
    # compare objective
    print("Extensive: ", extensive.ObjVal)
    print("Two-stage: ", production.MP.ObjVal)
    return


if __name__ == "__main__":
    main()
