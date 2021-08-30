import behavioral.state.states as st
import os


class Git:

    def __init__(self, path):
        self.state = st.Init(self)
        self.state.init(path)
        self.path = path

    def setState(self, state):
        self.state = state

    def add(self,file=False):
        self.state.add(file)

    def commit(self,name_commit):
        self.state.commit(name_commit)

    def push(self,branch):
        self.state.push(branch)

rep=Git('https://github.com/GushinDanil/New.git')
rep.add()
rep.commit('first commit')
rep.push('main')