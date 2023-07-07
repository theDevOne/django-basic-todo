from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from todolist.models import TodoItem
import random
from faker import Faker
fake = Faker()

User = get_user_model()

class Command(BaseCommand):
    help = "Create random user and todos"

    def handle(self, *args, **options):
        no_of_users = random.randint(5,10)

        print("Generating Data ...")

        for user in range(no_of_users):
            user = User.objects.create_user(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                username=fake.user_name(),
                password=fake.password(),
            )

            todos = []

            for i in range(random.randint(10,20)):
                string = fake.paragraph()
                todos.append(TodoItem(
                    name = string[:10],
                    description = string,
                    user = user,
                    completed = random.choice([True,False])
                ))

            TodoItem.objects.bulk_create(todos)

        self.stdout.write(
            self.style.SUCCESS('Successfully generate fake user and todos')
        )