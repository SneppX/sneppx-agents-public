from pathlib import Path

def test_at_least_one_agent_present():
    agents = list((Path(__file__).parent.parent / "agents").glob("*.md"))
    assert len(agents) >= 1
