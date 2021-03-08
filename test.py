from muzero import MuZero
mz = MuZero('anytrading')
mz.load_model(
   checkpoint_path=   'results/anytrading/2021-01-15--05-57-26/model.checkpoint',
   replay_buffer_path='results/anytrading/2021-01-15--05-57-26/replay_buffer.pkl',
)
result = mz.test(render=True, opponent="self", muzero_player=None)
print ('result',result)
