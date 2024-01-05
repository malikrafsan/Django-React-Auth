from dataclasses import dataclass
import enum


class Status(enum.Enum):
    TODO = 1
    DOING = 2
    DONE = 3

    def __str__(self):
        return self.name
    
    def to_str(self):
        return self.name


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: Status
    username: str

    @staticmethod
    def deserialize(task: list):
        return Task(
            id=task[0],
            username=task[1],
            title=task[2],
            content=task[3]
        )

    def change_status(self, status: Status):
        self.status = status

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'title': self.title,
            'description': self.description,
            'status': str(self.status)
        }
