import click

from crud.crud import create_user, get_user, get_all_users, update_user, delete_user

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
        # Add Nutrition logic here

    elif user_input == 3:
        click.secho("Exercise Options", fg='green')
        click.secho("1. Add Exercise Entry", fg='green')
        click.secho("2. View Exercise Entries", fg='yellow')
        # Add Exercise logic here

    elif user_input == 4:
        click.secho("Viewing Daily Summary...", fg='green')
        # Add summary logic here

    elif user_input == 5:
        click.secho("Exiting Health & Fitness Tracker. Goodbye!", fg='yellow')
        break

    else:
        click.secho("Invalid option. Please try again.", fg='red')
