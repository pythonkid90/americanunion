use separator::Separatable;

const CITIZENS: f64 = 59.693723;
const POSSIBLE_PERCENTAGE_CHANGE: f64 = 50.0 / 100.0;

fn main() {
    let representatives: f64 = CITIZENS * 1000000.0 / 50000.0;
    let representatives: i64 = representatives.round() as i64;
    
    let mut parties: [(&str, f64); 7]  = [("Normalist", 20.0), ("Lingist", 0.5), ("Center-Peace", 24.0), ("Capybara", 25.0), ("Vulture", 15.0), ("Economic Expansion", 5.0), ("Independent", 11.0)];

    let mut total = 0.0;

    // Randomly change party weights for variation.
    for party in &mut parties {
        let percentage_of_reps_change = (fastrand::f64() * POSSIBLE_PERCENTAGE_CHANGE * party.1) - (POSSIBLE_PERCENTAGE_CHANGE * party.1 * 0.50);

        (*party).1 = party.1 + percentage_of_reps_change;
        total += party.1;
    }

    // Make percentages out of representatives.
    let mut new_total = 0.0;

    for party in &mut parties {
        let percent_of_reps = (party.1) / total;
        (*party).1 = (percent_of_reps * representatives as f64).round();
        new_total += party.1;
    }

    // Fix rounding errors.
    let representative_difference = new_total as i64 - representatives;
    let mut change_amount = 1.0;
    if new_total as i64 > representatives {
        change_amount = -1.0;
    }

    for _ in 1..(representative_difference * (change_amount as i64) + 1) {
            let party_to_change = &mut parties[fastrand::usize(..parties.len())];
            (*party_to_change).1 += 1.0;
    }
    
    // Print final stats.
    print!("Fifth Medilli Senate Election (October 1, 2025)\n\nPopulation: {} \nRepresentatives/Districts: {representatives} \nSenate composition: ", (CITIZENS * 1000000.0).separated_string());

    for party in &mut parties {
        if party.0 == "Independent" {
            print!("and {} ({:.2}%) are {} members.", party.1 as i64, party.1 / representatives as f64 * 100.0, party.0);
        } else {
            print!("{} ({:.2}%) are {} members, ", party.1 as i64, party.1 / representatives as f64 * 100.0, party.0);
        }
    }
}

