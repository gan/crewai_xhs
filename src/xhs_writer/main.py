#!/usr/bin/env python
from xhs_writer.crew import XhsWriterCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    XhsWriterCrew().crew().kickoff(inputs=inputs)