# Claude AI helped with the developement of the frontend styling and visual elements/colors. All core logic, data structures, and program flow/function were designed and implemented by me. 
import html
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="FitRec — Fitness Activity Recommender",
    page_icon="",
    layout="centered",
)

def load_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');
        :root {
          --bg: #0a0a0a;
          --surface: #111111;
          --surface2: #1a1a1a;
          --border: rgba(255,255,255,0.07);
          --accent: #c8f560;
          --accent2: #f5a623;
          --text: #f0f0f0;
          --muted: #555;
          --muted2: #888;
        }
        html, body, [class*="css"] {
          font-family: 'DM Sans', sans-serif;
        }
        .stApp {
          background:
            linear-gradient(rgba(10,10,10,0.97), rgba(10,10,10,0.99)),
            linear-gradient(rgba(200,245,96,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(200,245,96,0.03) 1px, transparent 1px);
          background-size: auto, 60px 60px, 60px 60px;
          color: var(--text);
        }
        .block-container {
          max-width: 860px;
          padding-top: 2.5rem;
          padding-bottom: 4rem;
        }
        #MainMenu, header[data-testid="stHeader"], footer {
          display: none;
        }
        div[data-testid="stVerticalBlock"] > div:has(.app-shell) {
          width: 100%;
        }
        .app-shell {
          position: relative;
          z-index: 1;
        }
        .header {
          display: flex;
          align-items: flex-start;
          justify-content: space-between;
          margin-bottom: 4rem;
        }
        .logo {
          font-family: 'Bebas Neue', sans-serif;
          font-size: 2.2rem;
          letter-spacing: 0.08em;
          color: var(--accent);
          line-height: 1;
        }
        .logo span {
          color: var(--text);
        }
        .badge {
          font-family: 'DM Mono', monospace;
          font-size: 10px;
          font-weight: 500;
          letter-spacing: 0.1em;
          color: var(--muted2);
          background: var(--surface2);
          border: 1px solid var(--border);
          padding: 5px 10px;
          border-radius: 4px;
          text-transform: uppercase;
          margin-top: 4px;
        }
        .hero {
          margin-bottom: 3.5rem;
        }
        .hero-tag {
          font-family: 'DM Mono', monospace;
          font-size: 11px;
          letter-spacing: 0.12em;
          text-transform: uppercase;
          color: var(--accent);
          margin-bottom: 0.75rem;
          display: flex;
          align-items: center;
          gap: 8px;
        }
        .hero-tag::before {
          content: '';
          display: inline-block;
          width: 24px;
          height: 1px;
          background: var(--accent);
        }
        .hero h1 {
          font-family: 'Bebas Neue', sans-serif;
          font-size: clamp(3rem, 8vw, 5.5rem);
          line-height: 0.92;
          letter-spacing: 0.02em;
          color: var(--text);
          margin-bottom: 1rem;
        }
        .hero h1 em {
          font-style: normal;
          color: var(--accent);
        }
        .hero p {
          font-size: 15px;
          color: var(--muted2);
          max-width: 520px;
          line-height: 1.65;
        }
        .card {
          background: var(--surface);
          border: 1px solid var(--border);
          border-radius: 16px;
          padding: 2rem;
          margin-bottom: 2rem;
        }
        div[data-testid="stVerticalBlock"]:has(.controls-marker) {
          background: var(--surface);
          border: 1px solid var(--border);
          border-radius: 16px;
          padding: 2rem;
          margin-bottom: 2rem;
        }
        .card-label {
          font-family: 'DM Mono', monospace;
          font-size: 10px;
          letter-spacing: 0.14em;
          text-transform: uppercase;
          color: var(--muted);
          margin-bottom: 1rem;
        }
        .goal-card {
          background: var(--surface2);
          border: 1px solid var(--border);
          border-radius: 12px;
          padding: 1.15rem 1rem;
          min-height: 132px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          gap: 0.35rem;
          transition: all 0.2s ease;
        }
        .goal-card.active {
          border-color: var(--accent);
          background: rgba(200,245,96,0.08);
          box-shadow: 0 10px 28px rgba(200,245,96,0.1);
        }
        .goal-icon {
          font-size: 1.8rem;
        }
        .goal-name {
          font-family: 'Bebas Neue', sans-serif;
          font-size: 1.2rem;
          letter-spacing: 0.06em;
          color: var(--text);
        }
        .goal-card.active .goal-name {
          color: var(--accent);
        }
        .goal-sub {
          font-size: 11px;
          color: var(--muted2);
        }
        .time-wrap {
          display: flex;
          align-items: end;
          justify-content: space-between;
          margin-bottom: 0.5rem;
        }
        .time-label {
          font-size: 13px;
          font-weight: 500;
          color: var(--muted2);
        }
        .time-value {
          font-family: 'Bebas Neue', sans-serif;
          font-size: 2rem;
          color: var(--accent);
          line-height: 1;
        }
        .time-value span {
          font-family: 'DM Sans', sans-serif;
          font-size: 13px;
          color: var(--muted2);
          font-weight: 400;
          margin-left: 4px;
        }
        .mini-grid {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 0.75rem;
          margin: 1.2rem 0 1.6rem;
        }
        .mini-card {
          background: rgba(200,245,96,0.03);
          border: 1px solid var(--border);
          border-radius: 12px;
          padding: 1rem;
        }
        .mini-label {
          font-family: 'DM Mono', monospace;
          font-size: 10px;
          color: var(--muted2);
          letter-spacing: 0.08em;
          text-transform: uppercase;
          margin-bottom: 0.45rem;
        }
        .mini-value {
          font-size: 15px;
          font-weight: 500;
          color: var(--text);
        }
        .results-header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 1.25rem;
        }
        .results-title {
          font-family: 'Bebas Neue', sans-serif;
          font-size: 1.4rem;
          letter-spacing: 0.06em;
          color: var(--text);
        }
        .results-count {
          font-family: 'DM Mono', monospace;
          font-size: 11px;
          color: var(--muted2);
          background: var(--surface2);
          border: 1px solid var(--border);
          padding: 3px 10px;
          border-radius: 20px;
        }
        .activity-item {
          background: var(--surface);
          border: 1px solid var(--border);
          border-radius: 10px;
          padding: 1rem 1.25rem;
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 0.65rem;
        }
        .activity-num {
          font-family: 'DM Mono', monospace;
          font-size: 10px;
          color: var(--muted);
          width: 24px;
          text-align: right;
          flex-shrink: 0;
        }
        .activity-copy {
          flex: 1;
        }
        .activity-name {
          font-weight: 600;
          font-size: 15px;
          color: var(--text);
          margin-bottom: 0.15rem;
        }
        .activity-sub {
          font-size: 12px;
          color: var(--muted2);
          line-height: 1.5;
        }
        .activity-dur {
          font-family: 'DM Mono', monospace;
          font-size: 11px;
          color: var(--accent);
          background: rgba(200,245,96,0.08);
          padding: 3px 9px;
          border-radius: 20px;
          white-space: nowrap;
        }
        .rest-card {
          background: var(--surface);
          border: 1px solid rgba(245,166,35,0.3);
          border-radius: 10px;
          padding: 1.5rem;
          text-align: center;
        }
        .rest-icon {
          font-size: 2rem;
          margin-bottom: 0.5rem;
        }
        .rest-title {
          font-family: 'Bebas Neue', sans-serif;
          font-size: 1.4rem;
          color: var(--accent2);
          letter-spacing: 0.06em;
          margin-bottom: 0.25rem;
        }
        .rest-sub {
          font-size: 13px;
          color: var(--muted2);
        }
        .section-divider {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin: 2rem 0;
        }
        .section-divider span {
          font-family: 'DM Mono', monospace;
          font-size: 10px;
          color: var(--muted);
          text-transform: uppercase;
          letter-spacing: 0.12em;
          white-space: nowrap;
        }
        .section-divider::before, .section-divider::after {
          content: '';
          flex: 1;
          height: 1px;
          background: var(--border);
        }
        .code-panel {
          background: #0d0d0d;
          border: 1px solid var(--border);
          border-radius: 16px;
          overflow: hidden;
          margin-bottom: 2rem;
        }
        .code-topbar {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0.75rem 1.25rem;
          border-bottom: 1px solid var(--border);
          background: var(--surface);
        }
        .code-dots {
          display: flex;
          gap: 6px;
        }
        .code-dots span {
          width: 10px;
          height: 10px;
          border-radius: 50%;
          background: var(--border);
        }
        .code-lang {
          font-family: 'DM Mono', monospace;
          font-size: 11px;
          color: var(--muted2);
        }
        .code-body {
          padding: 1.25rem 1.5rem;
          overflow-x: auto;
        }
        .code-body pre {
          font-family: 'DM Mono', monospace;
          font-size: 12.5px;
          line-height: 1.75;
          color: #cdd6f4;
          white-space: pre-wrap;
        }
        .footer {
          margin-top: 2.5rem;
          padding-top: 2rem;
          border-top: 1px solid var(--border);
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 1rem;
          flex-wrap: wrap;
        }
        .footer-left {
          font-family: 'DM Mono', monospace;
          font-size: 11px;
          color: var(--muted);
        }
        .footer-rubric {
          display: flex;
          gap: 6px;
          flex-wrap: wrap;
        }
        .rubric-tag {
          font-family: 'DM Mono', monospace;
          font-size: 9px;
          letter-spacing: 0.08em;
          text-transform: uppercase;
          padding: 3px 8px;
          border-radius: 3px;
          border: 1px solid var(--border);
          color: var(--muted2);
        }
        .stButton > button {
          width: 100%;
          border-radius: 10px;
          border: 1px solid var(--border);
          background: var(--surface2);
          color: var(--text);
          font-family: 'DM Sans', sans-serif;
          font-weight: 500;
          min-height: 2.75rem;
        }
        .stButton > button:hover {
          border-color: rgba(200,245,96,0.35);
          color: var(--accent);
        }
        .stButton > button[kind="primary"] {
          background: var(--accent);
          color: #0a0a0a;
          border-color: var(--accent);
          font-family: 'Bebas Neue', sans-serif;
          font-size: 1.2rem;
          letter-spacing: 0.08em;
        }
        .stButton > button[kind="primary"]:hover {
          background: #d6ff6e;
          border-color: #d6ff6e;
          color: #0a0a0a;
        }
        .stSlider [data-baseweb="slider"] {
          padding-top: 0.2rem;
        }
        .stSlider [role="slider"] {
          box-shadow: 0 0 10px rgba(200,245,96,0.4);
          background: var(--accent);
        }
        .stSlider div[data-testid="stTickBar"] {
          display: none;
        }
        .stRadio label, .stSelectSlider label, .stCheckbox label {
          color: var(--muted2);
        }
        .stRadio [role="radiogroup"] {
          gap: 0.45rem;
        }
        .stRadio [role="radiogroup"] label {
          background: var(--surface2);
          border: 1px solid var(--border);
          border-radius: 999px;
          padding: 0.35rem 0.85rem;
        }
        .stAlert {
          background: rgba(245,166,35,0.08);
          border: 1px solid rgba(245,166,35,0.3);
          color: var(--text);
        }
        @media (max-width: 640px) {
          .header {
            flex-direction: column;
            gap: 0.75rem;
            margin-bottom: 2.5rem;
          }
          .card {
            padding: 1.25rem;
          }
          .mini-grid {
            grid-template-columns: 1fr;
          }
          .results-header {
            align-items: flex-start;
            gap: 0.75rem;
            flex-direction: column;
          }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_state() -> None:
    defaults = {
        "goal": None,
        "minutes": 30,
        "intensity": "Moderate",
        "location": "Any",
        "recovery_block": True,
        "submitted": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value



ACTIVITIES = [
    {"name": "Running", "goal": "cardio", "duration": 30, "intensity": 2, "locations": ["Outdoor", "Gym"], "benefit": "Steady endurance boost", "gear": "Shoes"},
    {"name": "Jump Rope", "goal": "cardio", "duration": 15, "intensity": 3, "locations": ["Home", "Gym", "Outdoor"], "benefit": "Quick calorie burn", "gear": "Rope"},
    {"name": "Cycling", "goal": "cardio", "duration": 45, "intensity": 2, "locations": ["Outdoor", "Gym"], "benefit": "Low-impact stamina work", "gear": "Bike"},
    {"name": "High Intensity Sprints", "goal": "cardio", "duration": 20, "intensity": 3, "locations": ["Outdoor", "Gym"], "benefit": "Explosive conditioning", "gear": "Track"},
    {"name": "Push-Ups", "goal": "strength", "duration": 10, "intensity": 1, "locations": ["Home", "Gym"], "benefit": "Upper-body activation", "gear": "Bodyweight"},
    {"name": "Dumbbell Curls", "goal": "strength", "duration": 20, "intensity": 2, "locations": ["Home", "Gym"], "benefit": "Arm and grip strength", "gear": "Dumbbells"},
    {"name": "Squats", "goal": "strength", "duration": 15, "intensity": 2, "locations": ["Home", "Gym"], "benefit": "Lower-body power", "gear": "Bodyweight"},
    {"name": "Bench Press", "goal": "strength", "duration": 30, "intensity": 3, "locations": ["Gym"], "benefit": "Chest and triceps strength", "gear": "Bench + bar"},
    {"name": "Yoga", "goal": "flexibility", "duration": 30, "intensity": 1, "locations": ["Home", "Gym"], "benefit": "Mobility and breathing", "gear": "Mat"},
    {"name": "Stretching", "goal": "flexibility", "duration": 10, "intensity": 1, "locations": ["Home", "Gym", "Outdoor"], "benefit": "Recovery and range of motion", "gear": "None"},
    {"name": "Pilates", "goal": "flexibility", "duration": 45, "intensity": 2, "locations": ["Home", "Gym"], "benefit": "Core control and posture", "gear": "Mat"},
    {"name": "Row Intervals", "goal": "cardio", "duration": 25, "intensity": 3, "locations": ["Gym"], "benefit": "Full-body cardio effort", "gear": "Row machine"},
    {"name": "Kettlebells", "goal": "strength", "duration": 25, "intensity": 3, "locations": ["Gym", "Home"], "benefit": "Power and conditioning mix", "gear": "Kettlebell"},
    {"name": "Mobility Stretching", "goal": "flexibility", "duration": 20, "intensity": 2, "locations": ["Home", "Outdoor"], "benefit": "Joint prep and control", "gear": "Mat"},
]


GOAL_META = {
    "cardio": {"icon": "RUN", "name": "Cardio", "sub": "Endurance & burn"},
    "strength": {"icon": "LIFT", "name": "Strength", "sub": "Muscle & power"},
    "flexibility": {"icon": "FLOW", "name": "Flexibility", "sub": "Stretch & recover"},
}


INTENSITY_VALUE = {"Low": 1, "Moderate": 2, "High": 3}


def recommend_activities(goal: str, minutes: int, intensity: str, location: str, recovery_block: bool, activity_list: list[dict]) -> tuple[list[dict], dict]:
    target_intensity = INTENSITY_VALUE[intensity]
    usable_minutes = max(minutes - (10 if recovery_block else 0), 5)
    ranked = []
    for activity in activity_list:
        if activity["goal"] == goal:
            if activity["duration"] <= usable_minutes:
                if location == "Any" or location in activity["locations"]:
                    intensity_gap = abs(activity["intensity"] - target_intensity)
                    spare_minutes = usable_minutes - activity["duration"]
                    score = 100 - (intensity_gap * 15) - spare_minutes
                    ranked.append(
                        {
                            "name": activity["name"],
                            "duration": activity["duration"] + (10 if recovery_block else 0),
                            "focus": activity["benefit"],
                            "gear": activity["gear"],
                            "location": ", ".join(activity["locations"]),
                            "score": score,
                            "recovery": "Includes 5 min warm-up + 5 min cooldown" if recovery_block else "Pure workout block",
                        }
                    )
    ranked.sort(key=lambda item: (-item["score"], item["duration"], item["name"]))
    if not ranked:
        return [], {
            "available": usable_minutes,
            "match_count": 0,
            "headline": "No exact fit",
            "summary": "Your current filters are tight, so a recovery-focused day is the best recommendation.",
        }
    recommendations = ranked[:3]
    return recommendations, {
        "available": usable_minutes,
        "match_count": len(recommendations),
        "headline": recommendations[0]["name"],
        "summary": f"{recommendations[0]['name']} is the closest match for your goal, time, and training setup.",
    }


def build_weekly_plan(goal: str, recommendations: list[dict]) -> list[str]:
    if not recommendations:
        return ["Mon: Recovery walk", "Wed: Mobility reset", "Fri: Full rest"]
    labels = {
        "cardio": ["Mon", "Thu", "Sat"],
        "strength": ["Tue", "Thu", "Sun"],
        "flexibility": ["Mon", "Wed", "Sat"],
    }
    plan = []
    for index, day in enumerate(labels[goal]):
        activity = recommendations[index % len(recommendations)]
        plan.append(f"{day}: {activity['name']} for {activity['duration']} min")
    return plan


def rubric_excerpt() -> str:
    lines = Path(__file__).read_text().splitlines()
    targets = ("# List 1", "# Procedure 1", "# List 2", "# Procedure 2")
    selected = []
    capture_until = -1
    for index, line in enumerate(lines):
        if any(line.startswith(target) for target in targets):
            capture_until = max(capture_until, index + 8)
        if index <= capture_until:
            selected.append(line)
    return "\n".join(selected)


def render_header() -> None:
    st.markdown(
        """
        <div class="app-shell">
          <div class="header">
            <div class="logo">Fit<span>Rec</span></div>
            <div class="badge">AP CSP · CPT Project</div>
          </div>
          <div class="hero">
            <div class="hero-tag">Fitness Activity Recommender</div>
            <h1>FIND YOUR<br><em>WORKOUT</em></h1>
            <p>Enter your fitness goal and available time. The program filters from a list of activities and recommends the best match for you, then builds a simple plan around that choice.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_goal_selector() -> None:
    st.markdown('<div class="card-label">01 — Choose your goal</div>', unsafe_allow_html=True)
    columns = st.columns(3)
    for column, key in zip(columns, GOAL_META):
        with column:
            meta = GOAL_META[key]
            active_class = " active" if st.session_state.goal == key else ""
            st.markdown(
                f"""
                <div class="goal-card{active_class}">
                  <div class="goal-icon">{meta["icon"]}</div>
                  <div class="goal-name">{meta["name"]}</div>
                  <div class="goal-sub">{meta["sub"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Select {meta['name']}", key=f"goal_{key}", use_container_width=True):
                st.session_state.goal = key


def render_controls() -> None:
    controls = st.container()
    with controls:
        st.markdown('<div class="controls-marker"></div>', unsafe_allow_html=True)
        render_goal_selector()
        st.markdown(
            f"""
            <div class="time-wrap">
              <div class="card-label" style="margin-bottom:0;">02 — Available time</div>
              <div class="time-value">{st.session_state.minutes} <span>min</span></div>
            </div>
            <div class="time-label">How long do you have?</div>
            """,
            unsafe_allow_html=True,
        )
        st.slider(
            "Available time in minutes",
            min_value=5,
            max_value=60,
            step=5,
            key="minutes",
            label_visibility="collapsed",
        )
        st.markdown('<div class="card-label" style="margin-top:1.5rem;">03 — Tune your session</div>', unsafe_allow_html=True)
        option_left, option_right = st.columns(2)
        with option_left:
            st.select_slider(
                "Intensity",
                options=["Low", "Moderate", "High"],
                key="intensity",
            )
            st.checkbox("Add a warm-up and cooldown block", key="recovery_block")
        with option_right:
            st.radio(
                "Workout location",
                options=["Any", "Home", "Gym", "Outdoor"],
                key="location",
                horizontal=True,
            )
        if st.button("Get Recommendations", type="primary", use_container_width=True):
            st.session_state.submitted = True


def render_results(goal: str, recommendations: list[dict], summary: dict) -> None:
    st.markdown(
        f"""
        <div class="results-header">
          <div class="results-title">Recommended Workouts</div>
          <div class="results-count">{summary["match_count"]} activit{'y' if summary["match_count"] == 1 else 'ies'}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if not recommendations:
        st.markdown(
            """
            <div class="rest-card">
              <div class="rest-icon">REST</div>
              <div class="rest-title">Recovery Day</div>
              <div class="rest-sub">No activities fit the full set of filters right now. Ease back, recover, and try a wider time or location range.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return
    st.markdown(
        f"""
        <div class="mini-grid">
          <div class="mini-card">
            <div class="mini-label">Best Match</div>
            <div class="mini-value">{summary["headline"]}</div>
          </div>
          <div class="mini-card">
            <div class="mini-label">Workout Block</div>
            <div class="mini-value">{st.session_state.minutes} min selected</div>
          </div>
          <div class="mini-card">
            <div class="mini-label">Filter Snapshot</div>
            <div class="mini-value">{st.session_state.intensity} / {st.session_state.location}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    for index, activity in enumerate(recommendations, start=1):
        st.markdown(
            f"""
            <div class="activity-item">
              <div class="activity-num">{index:02d}</div>
              <div class="activity-copy">
                <div class="activity-name">{activity["name"]}</div>
                <div class="activity-sub">{activity["focus"]} · {activity["gear"]} · {activity["location"]} · {activity["recovery"]}</div>
              </div>
              <div class="activity-dur">{activity["duration"]} min</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    left, right = st.columns(2)
    with left:
        st.markdown(
            f"""
            <div class="card">
              <div class="card-label">Why this works</div>
              <div class="mini-value" style="font-size:1rem;">{summary["summary"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        weekly_plan = build_weekly_plan(goal, recommendations)
        plan_html = "".join(
            f'<div class="activity-sub" style="padding:0.28rem 0;color:var(--text);">{html.escape(item)}</div>'
            for item in weekly_plan
        )
        st.markdown(
            f"""
            <div class="card">
              <div class="card-label">3-Day Rotation</div>
              {plan_html}
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_code_panel() -> None:
    code_block = html.escape(rubric_excerpt())
    st.markdown(
        """
        <div class="section-divider"><span>Source Code</span></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="code-panel">
          <div class="code-topbar">
            <div class="code-dots"><span></span><span></span><span></span></div>
            <div class="code-lang">main.py</div>
            <div class="code-lang">rubric markers</div>
          </div>
          <div class="code-body"><pre>{code_block}</pre></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        """
        <div class="footer">
          <div class="footer-left">AP CSP · CPT Rubric Coverage</div>
          <div class="footer-rubric">
            <div class="rubric-tag">Input/Output</div>
            <div class="rubric-tag">List</div>
            <div class="rubric-tag">Procedure</div>
            <div class="rubric-tag">Sequencing</div>
            <div class="rubric-tag">Selection</div>
            <div class="rubric-tag">Iteration</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    load_styles()
    initialize_state()
    render_header()
    render_controls()
    if st.session_state.submitted:
        if not st.session_state.goal:
            st.warning("Choose a goal first so the recommender can filter the activity list.")
        else:
            recommendations, summary = recommend_activities(
                st.session_state.goal,
                st.session_state.minutes,
                st.session_state.intensity,
                st.session_state.location,
                st.session_state.recovery_block,
                ACTIVITIES,
            )
            render_results(st.session_state.goal, recommendations, summary)
    render_code_panel()
    render_footer()


main()
