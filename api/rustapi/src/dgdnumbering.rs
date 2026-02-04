use num_base::Based;
use chrono::Local;

fn main() {
    let date = format!("{}", Local::now().date_naive().format("%Y%m%d"));

    let num = Based::new(date, 10).to(36).expect("We couldn't format the date for some reason. I don't know what happened.").val.to_uppercase();
    println!("{}", num);
}