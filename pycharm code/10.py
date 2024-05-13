class Job:
	def __init__(self, taskId, deadline, profit):
		self.taskId = taskId
		self.deadline = deadline
		self.profit = profit


# Function to schedule jobs to maximize profit
def scheduleJobs(jobs, T):
	profit = 0
	# list to store used and unused slots info
	slot = [-1] * T
	# arrange the jobs in decreasing order of their profits
	jobs.sort(key=lambda x: x.profit, reverse=True)

	# consider each job in decreasing order of their profits
	for job in jobs:
		# search for the next free slot and map the task to that slot
		for j in reversed(range(job.deadline)):
			if j < T and slot[j] == -1:
				slot[j] = job.taskId
				profit += job.profit
				break

	print('The scheduled jobs are', list(filter(lambda x: x != -1, slot)))
	print('The total profit earned is', profit)



jobs = [
		Job(1, 1, 3), Job(2, 3, 25), Job(3, 2, 1), Job(4, 1, 6),Job(5, 2, 30)
]
T = len(jobs)
scheduleJobs(jobs, T)
