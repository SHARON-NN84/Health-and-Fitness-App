

import click

from crud.crud import (
    create_user, get_user, get_all_users, 
    update_user, delete_user, get_nutrition_entries, 
    add_nutrition_entry, get_exercise_sessions, add_exercise_session,
    get_health_metrics, add_health_metric)

while True:
    click.secho("Welcome to Health & Fitness Tracker", fg='blue')
    click.secho("Select Option to Proceed", fg='blue')
    click.secho("1. Users", fg='green')
    click.secho("2. Nutrition", fg='green')
    click.secho("3. Exercise", fg='green')
    click.secho("4. View Daily Summary", fg='green')
    click.secho("5. Exit", fg='yellow')

    user_input = click.prompt("Select Option", type=int)
    click.secho(f"You selected option {user_input}", fg='cyan')

    if user_input == 1:
        click.secho("User Options", fg='blue')
        click.secho("1. Add New User", fg='green')
        click.secho("2. View All Users", fg='yellow')
        click.secho("3. Update User", fg='green')
        click.secho("4. Delete User", fg='red')

        user_option = click.prompt("Select User Option", type=int)

        if user_option == 1:
            click.secho("Adding New User...", fg="yellow")
            name = click.prompt("Enter Name")
            age = click.prompt("Enter Age", type=int)
            weight = click.prompt("Enter Weight (kg)", type=float)
            height = click.prompt("Enter Height (cm)", type=float)
            user = create_user(name, age, weight, height)
            click.secho(f"User created: {user.name}, Age: {user.age}, Weight: {user.weight}kg, Height: {user.height}cm", fg="blue")

        elif user_option == 2:
            click.secho("Fetching All Users...", fg="green")
            users = get_all_users()
            for user in users:
                click.secho(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}, Weight: {user.weight}kg, Height: {user.height}cm", fg="blue")

        elif user_option == 3:
            user_id = click.prompt("Enter User ID to update", type=int)
            name = click.prompt("Enter New Name", default="")
            age = click.prompt("Enter New Age", type=int, default=0)
            weight = click.prompt("Enter New Weight (kg)", type=float, default=0.0)
            height = click.prompt("Enter New Height (cm)", type=float, default=0.0)
            updated_user = update_user(user_id, name, age, weight, height)
            click.secho(f"User updated: {updated_user.name}, Age: {updated_user.age}, Weight: {updated_user.weight}kg, Height: {updated_user.height}cm", fg="blue")

        elif user_option == 4:
            user_id = click.prompt("Enter User ID to delete", type=int)
            delete_user(user_id)
            click.secho(f"User with ID {user_id} deleted.", fg="red")

    elif user_input == 2:
        click.secho("Nutrition Options", fg='green')
        click.secho("1. Add Nutrition Entry", fg='green')
        click.secho("2. View Nutrition Entries", fg='yellow')

        nutrition_option = click.prompt("Select Nutrition Option", type=int)

        if nutrition_option == 1:
            click.secho("Adding Nutrition Entry...", fg="yellow")
            user_id = click.prompt("Enter User ID", type=int)
            food = click.prompt("Enter Food Name")
            calories = click.prompt("Enter Calories", type=float)
            protein = click.prompt("Enter Protein (g)", type=float, default=0.0)
            carbs = click.prompt("Enter Carbohydrates (g)", type=float, default=0.0)
            fat = click.prompt("Enter Fat (g)", type=float, default=0.0)
            entry = add_nutrition_entry(user_id, food, calories, protein, carbs, fat)
            click.secho(f"Added Nutrition Entry: {entry.food} ({entry.calories} kcal)", fg="blue")

        elif nutrition_option == 2:
            user_id = click.prompt("Enter User ID", type=int)
            date_str = click.prompt("Enter Date (YYYY-MM-DD) or press Enter for all", default="", show_default=False)
            entries = get_nutrition_entries(user_id, date_str if date_str else None)
            for e in entries:
                click.secho(f"{e.timestamp} - {e.food}: {e.calories} kcal, P:{e.protein}g C:{e.carbs}g F:{e.fat}g", fg="blue")


    elif user_input == 3:
        click.secho("Exercise Options", fg='green')
        click.secho("1. Add Exercise Session", fg='green')
        click.secho("2. View Exercise Sessions", fg='yellow')

        exercise_option = click.prompt("Select Exercise Option", type=int)

        if exercise_option == 1:
            click.secho("Adding Exercise Session...", fg="yellow")
            user_id = click.prompt("Enter User ID", type=int)
            type_ = click.prompt("Enter Exercise Type (e.g. Running, Cycling)")
            duration = click.prompt("Enter Duration (minutes)", type=int)
            calories_burned = click.prompt("Enter Calories Burned", type=float)
            notes = click.prompt("Enter Notes", default="")
            session_entry = add_exercise_session(user_id, type_, duration, calories_burned, notes)
            click.secho(f"Exercise Added: {session_entry.type}, {session_entry.duration} min, {session_entry.calories_burned} kcal", fg="blue")

        elif exercise_option == 2:
            user_id = click.prompt("Enter User ID", type=int)
            date_str = click.prompt("Enter Date (YYYY-MM-DD) or press Enter for all", default="", show_default=False)
            sessions = get_exercise_sessions(user_id, date_str if date_str else None)
            for s in sessions:
                click.secho(f"{s.timestamp} - {s.type}: {s.duration} min, {s.calories_burned} kcal", fg="blue")


    elif user_input == 4:
        click.secho("Viewing Daily Summary...", fg='green')
        user_id = click.prompt("Enter User ID", type=int)
        date_str = click.prompt("Enter Date (YYYY-MM-DD)", type=str)

        nutrition_entries = get_nutrition_entries(user_id, date_str)
        exercise_sessions = get_exercise_sessions(user_id, date_str)
        health_metrics = get_health_metrics(user_id, date_str)

        # Summaries
        total_calories_in = sum(n.calories for n in nutrition_entries)
        total_calories_out = sum(e.calories_burned for e in exercise_sessions)

        click.secho("------ DAILY SUMMARY ------", fg="cyan")
        click.secho(f"Nutrition: {len(nutrition_entries)} entries, {total_calories_in} kcal consumed", fg="blue")
        click.secho(f"Exercise: {len(exercise_sessions)} sessions, {total_calories_out} kcal burned", fg="blue")

        if health_metrics:
            latest = health_metrics[0]
            click.secho(f"Latest Health Metric: Weight={latest.weight}kg, BP={latest.blood_pressure}, HR={latest.heart_rate}", fg="blue")
        else:
            click.secho("No health metrics recorded.", fg="red")


    elif user_input == 5:
        click.secho("Exiting Health & Fitness Tracker. Goodbye!", fg='yellow')
        break

    else:
        click.secho("Invalid option. Please try again.", fg='red')