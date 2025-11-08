import os

from scoring import compute_score

# TODO: Change this to your team name
MY_TEAM_NAME = "sample_submission"

SUBMISSIONS_ROOT = "submissions"


def evaluate_all_datasets(team_name):
    """
    Runs evaluation on all 10 datasets for a given team.
    Returns (total_score, dataset_scores).
    """
    total_score = 0
    dataset_scores = {}
    print(f"\n=== Evaluating Team: {team_name} ===\n")

    for dataset_id in range(1, 10 + 1):
        inputs_path = f"datasets/dataset_{dataset_id}/inputs.csv"
        config_path = os.path.join(SUBMISSIONS_ROOT, team_name, f"dataset_{dataset_id}/box_configurations.csv")
        alloc_path = os.path.join(SUBMISSIONS_ROOT, team_name, f"dataset_{dataset_id}/box_allocations.csv")

        # TODO: Change the demand_path to the data you forecast for your experimentation
        demand_path = f"datasets_2025/dataset{dataset_id}_year2025.csv"

        try:
            score = compute_score(inputs_path, config_path, alloc_path, demand_path)
            print(f"📊 Dataset {dataset_id}: Score = {score}")
        except Exception as e:
            print(f"❌ Dataset {dataset_id}: Error - {e}")
            score = -1e9

        dataset_scores[f"dataset{dataset_id}"] = score
        total_score += score

    print(f"🏁 Combined Total Score: {total_score}")
    return total_score, dataset_scores


if __name__ == '__main__':
    evaluate_all_datasets(team_name=MY_TEAM_NAME)
