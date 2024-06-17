from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from xhs_writer.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class XhsWriterCrew():
	"""XhsWriter crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tool=[],
			verbose=True
		)

	@agent
	def seo_specialist(self) -> Task:
		return Task(
			config=self.agents_config['seo_specialist'],
			verbose=True
		)

	@agent
	def content_strategist(self) -> Task:
		return Task(
			config=self.agents_config['content_strategist'],
			verbose=True
		)

	@agent
	def social_media_analyst(self) -> Task:
		return Task(
			config=self.agents_config['social_media_analyst'],
			verbose=True
		)

	@agent
	def image_describer(self) -> Task:
		return Task(
			config=self.agents_config['image_describer'],
			verbose=True,
			allow_delegation=False
		)

	@task
	def market_research(self) -> Task:
		return Task(
			config=self.tasks_config['market_research'],
			verbose=True
		)

	@task
	def market_research(self) -> Task:
		return Task(
			config=self.tasks_config['market_research'],
			agent=self.market_researcher,
			output_file='market_research.md',
		)

	@task
	def content_strategy(self) -> Task:
		return Task(
			config=self.tasks_config['content_strategy'],
			agent=self.content_strategist,
			output_file='content_strategy.md',
		)

	@task
	def seo_optimization(self) -> Task:
		return Task(
			config=self.tasks_config['seo_optimization'],
			agent=self.seo_specialist,
			output_file='seo_optimization.md',
		)

	@task
	def social_media_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['social_media_analysis'],
			agent=self.social_media_analyst,
			output_file='social_media_analysis.md',
		)

	@task
	def image_description(self) -> Task:
		return Task(
			config=self.tasks_config['image_description'],
			agent=self.image_describer,
			output_file='image_description.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the XhsWriter crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)