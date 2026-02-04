use std::collections::HashMap;

const HOUSE_TOTAL: i32 = 3860;
const HOUSE_WEIGHT: f64 = 45.0;
const PEOPLE_WEIGHT: f64 = 20.0;
const PRESIDENT_WEIGHT: f64 = 10.0;
const VICE_WEIGHT: f64 = 5.0;
const ADVISOR_WEIGHT: f64 = 20.0;


fn main() {
    let mut options:HashMap<&str, (f64, f64)> = HashMap::from([
    ("house", (50.0, 40.0)),
    ("people", (40.0, 24.0)),
    ("president", (100.0, 0.0)),
    ("vice", (0.0, 0.0)),
    ("advisors", (30.0, 30.0))
    ]);

    for (_key, option) in options.iter_mut() {
        let chance_score = fastrand::f64() * option.1;
        let percentage = ((option.0 + chance_score) * 100.0).round() / 100.0;

        option.0 = percentage;
    }
    let representatives = (options["house"].0 / 100.0 * HOUSE_TOTAL as f64).round();
    let rep_percent = representatives / HOUSE_TOTAL as f64 * 100.0;
    let president_approval = if options["president"].0 == 100.0 { "approved" } else { "did not approve" };
    let vice_approval = if options["vice"].0 == 100.0 { "approved" } else { "did not approve" };

    println!("Voting: {representatives}/{HOUSE_TOTAL} house members approved it ({rep_percent:.2}%), {}% of the people who voted on it approved it, the president \
    (Jaylen) {president_approval} it, the vice president (Jones) {vice_approval} it, and {}% of the advisors approved it.", options["house"].0, options["advisors"].0);
    println!("Doing the math with the weights,  {representatives}/{HOUSE_TOTAL} house members approved it ({rep_percent:.2}%), {}% of the people who voted on it approved it, the president \
    (Jaylen) {president_approval} it, the vice president (Jones) {vice_approval} it, and {}% of the advisors approved it.", options["house"].0, options["advisors"].0);
    // let first_place_score = top_two[0].1;
    // let first_place_name = top_two[0].0;
    // let second_place_score = top_two[1].1;
    // let second_place_name = top_two[1].0;

    // let threshold = ((first_place_score - (first_place_score * 0.02)) * 100.0).round() / 100.0;

    // let percent_first_ranked_over = ((first_place_score + (fastrand::f64() * 14.0) + 42.0) * 100.0).round() / 100.0;
    // let percent_second_total_ranked_over = (((fastrand::f64() * 6.0) + 94.0) * 100.0).round() / 100.0 - percent_first_ranked_over;
    // let winner = if percent_first_ranked_over > percent_second_total_ranked_over {first_place_name} else {second_place_name};

    // println!("Top two - {first_place_name}: {first_place_score}/5, {second_place_name}: {second_place_score}/5. For a co-presidency, the rule is \
    // that the second placing candidate must be within 2% of the winning candidate (we do not allow three presidents).\n");

    // if second_place_score > threshold {
    //     println!("{second_place_name}'s score is greater than the threshold of {threshold:.2}, so we will have co-presidents!");
    // } else {
    //     println!("{second_place_name}'s score did not meet the threshold of {threshold:.2}. \
    //             Under STAR voting, the winner is determined by seeing what percentage of people rank {first_place_name} over {second_place_name} \
    //             and what percentage rank {second_place_name} over {first_place_name}. {percent_first_ranked_over:.2}% of people ranked {first_place_name} \
    //             over {second_place_name}, \
    //             while {percent_second_total_ranked_over:.2}% ranked {second_place_name} over {first_place_name}.");
    //     println!("This means {winner} is the President of the United Cold Nation!")
    // }
}