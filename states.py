from abc import abstractmethod, ABC
import os


class GitStates(ABC):
    def __init__(self, git):
        self.git = git

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def push(self):
        pass


class Init(GitStates):
    def init(self, path):
        os.system('git init')
        self.git.setState(Add(self.git))

    def add(self):
        pass

    def commit(self):
        pass

    def push(self):
        pass


class Add(GitStates):

    def init(self):
        pass


    def add(self,file=False):
        if file:
            os.system(f'git add {file}')
        else:
            os.system('git add .')
        self.git.setState(Commit(self.git))

    def commit(self):
        pass

    def push(self):
        pass


class Commit(GitStates):

    def init(self):
        pass

    def add(self):
        pass

    def change_rep(self):
        self.git.setState(Add(self.git))


    def commit(self,name_commit):
        os.system(f'git commit -m "{name_commit}"')
        self.git.setState(Push(self.git))


    def push(self):
        pass


class Push(GitStates):

    def init(self):
        pass

    def add(self):
        pass

    def commit(self):
        pass

    def push(self,branch):
        os.system(f'git branch -M {branch}')
        os.system(f'git remote add origin {self.git.path}')
        os.system(f'git push -u origin {branch}')
        self.git.setState(Add(self.git))
