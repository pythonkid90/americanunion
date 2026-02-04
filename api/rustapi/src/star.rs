const OPTIONS: [(&str, f64, f64); 14]  = [
("Arjun (Vulture) - Arjun Thimmakondu is running for reelection in the UCN! After a very innovative first term, possibly the most innovative \
in UCN history, Arjun is ready for more! He promises giving more government money for science, something that he has shown to be very enthusiastic about after the \
quantum computing and biotech from last term. He also plans to increase space exploration and try to build a small percentage of a swarm encompassing the sun to get \
almost unlimited energy. This will take many years to even get started, and it will take hundreds of years to complete, but we can reap in the benefits immediately if \
we just build a small amount. Needless to say, this is an ambitious feat but could make the UCN a leader in space exploration.",
3.9, 1.05),
("Parks (Vulture) - Although former president Tasha Parks lost the most recent UCN election, possibly due to Arjun, she has kept increasing the size of the Vulture party \
with campaigns centering on the entire party and even the Capybaras, not just her. She doesn't plan to enact any policies herself, and will ask her collegues for policies \
to get the best of many worlds. She also plans to allow citizens to vote for more policies than ever, allowing the people to choose what they want for their country. \
Because President Morgan is retiring, Parks will continue the trade deals with Couria and other nations to ensure good relationships with as much of the world as possible \
working together to give the best for all nations involved.",
3.8, 1.15),
("Jones (CP) - Zachary Jones has one of the best chances this time to win the UCN election, after an extensive campaign for the past 2-3 months. He is more confident than \
ever and is leaning much into the 'regular guy' persona in order to strengthen his 'Voice of Reason' slogan. He says that he is not just for the CP party, but for the \
nation as a whole. He believes that an ideal president is one who is not afraid to get stuff done and talks to the people often, not just in rallies, but in regular, \
even casual, conversations with the people to determine what to do in his term(s).",
4.2, 0.7),
("Adams (CP) - Jack Adams, like Arjun, wants to fund science and technology a huge amount in his term, however he wants to look more at the long-term impact of policies \
before 'vulturing' it out immedietly, calling it an 'ethical' approach. His main selling point this election is social work, as he wants to end wealth inequality once \
and for all. He wants to run trials on tons of different approaches to do this, ultimatley choosing the best onces to roll out for the entire nation. He even plans to \
introduce some of his best policies to the rest of the world. He is intentionally being vague so that he has room to change and innovate and give the people a say.",
3.7, 1.2),
("Yvan (Normalist) - Fran Yvan is a a more progressive Normalist who takes the rigidity of Normalism and adding Capybara-style innovation, giving the stability that \
Vultures and Capybaras, and even CPs fail to do. Peace is the biggest point in his campaign, believing that the nation needs to 'return to its roots' and follow AUT 8 \
more than ever. Three of his more specific policies that he is campaigning on are giving tax benefits to harder and poorer people, giving assistance to small businesses \
so that monopolices cannot thrive as well, and creating new public nature spaces, sidewalks, zoos, and entertainment spaces to make the great outdoors more appealing.",
3.6, 1.3),
("Eve (EEP) - Shaylyn Eve has switched to the EEP as the party gains prominence, and wants to become the 'next Arjun'. She wants to create more effective vaccienese and \
begin eradicating diseases in the UCN, beginning a multi-decade long effort. She also plans to buy land in Africa for the UCN, while keeping the native population happy, \
the UCN getting great trade deals out of it.",
2.2, 2.75),
("Justice (Capybara) - Steven Justice is trying again, despite the ultra-competitive environment in these recent elections, emphasizing that jails and prisions will be \
more humane, but of course not making it too comfortable, but giving more lessons on why and how to do better instead of just having people serving time. In addition to \
this, he will reduce unjust sentences for these people, and settle things on a case-by-case basis more often with a brand new reformed judicial system. He also plans to \
focus a lot on street safety, making road signs more readable, making the road code more strict, lowering speed limits in residential areas, adding roundabouts when needed \
and so much more.",
3.6, 1.4),
("Singh (CP) - Alejandra Singh, despite getting the smallest voting portion in the previous election, is happier than ever, characterizing herself as a very joyful \
leader who wants nothing more than to spread that joy to the citizens. She still leads the Nature Department of the Union, and is the strongest advocate for adding more parks \
and expanding many parks in the nation, making depressing industrial cities less depressing. She also is one of the biggest advocates for the environment
therefore she focuses on creating more open spaces to preserve nature from ever-expanding cities, also incorporating more nature into the cities.",
3.9, 1.0),
("Burnett (Capybara) - Virgil Burnett is a young Union leader of space exploration, leader of the space portion of the Union Air and Space Department, \
and wants to send the first super-heavy launch vehicle to Mars by the end of the decade. He is a visionary and believes that the cost of spaceflight could be lowered a lot with \
creation of space tethers and the first steps toward a moon base. He has been working hard as the Union department leader, and will continue Morgan's policies like cracking down on large \
businesses, especially the company  Big Pharma Inc.",
4.5, 0.3),
("Wilkins (EEP) - Jared Wilkins is focusing even more on welfare and justice for the poor and discriminated against in order to win this time. He finds that racial \
minorities in the UCN still face discriminaition, even in the big cities, and he plans to introduce a load of stricter laws to prevent that. He also promises to do even more \
with small businesses, creating a world where it's not just the big companies creating and controlling everything. As an addition to his welfare policies, he wants to establish
trade deals and relations with poorer nations, also helping the poorer nation become richer, as well as maintaing the prosperity of the UCN.",
3.2, 1.7),
("Turner (Normalist) - Amélia Turner runs on a campaign of smaller government and more power for the people. She believes in minimal laws yet harsh punishments and free \
speech first and foremost, and wants to make the UCN a great world superpower like Jonah. She is a very charismatic leader who many find charming, and she has developed \
a very devoted following. She also aims to reduce government spending and have stricter immigration policies. She calls herself a very strong patriot, and her followers \
seem to agree.",
3.2, 1.8),
("Jaylen (Capybara) - Marcelin Jaylen is a strong debator and a strong political leader with past experience in politics, specifically in Medilli's senate, being one of the top \
senators. She believes that it isn't the president that should get all the power, and plans to spread out the work among the UCN's representatives, giving many of her duties \
to them. She sees herself as a leader that will keep the people innovating, not the innovator, since nobody can do everything, and 'presidents are doing way too much'. ",
3.0, 1.9),
("Linton (EEP) - Kenneth Linton is a strong expansionist, planning to (mostly) peacefully expand the UCN's borders beyond its current standing, which would involve teaming \
up with Colony Freezing and expanding south to Kye's, creating one big nation surpassing Jonah in strength for the first time since the Third Jonah Empire. He believes \
that this will create a peaceful and prosperous nation, being very rich with a great military.",
1.0, 4.0),
("Bryony (Independent) - Dani Bryony is our final candidate here today, who believes that the only way to prevent the political divide from widening like it has been in Arjun's \
Colony is to band together and support neutral policies. He campaigns that 'you shouldn't let others decide how YOU vote. The power is in you.' He has policies like disbanding \
huge companies and free speech, while keeping the government efficient while still having pax (Latin word for peace). He is anti-war and believes in a new justice system. Some \
have compared him to Colony Freezing's 'unicandidate', but he says that he is much more focused and isn't just combining everything into 'one weird thing'. ",
2.2, 2.8)];


fn main() {
   let mut top_two: [(&str, f64); 2] = [("0", 0.0), ("0", 0.0)];


   for option in OPTIONS {
       let chance_score = fastrand::f64() * option.2;


       let option_info: Vec<&str> = option.0.split(" - ").collect();
       let score = ((option.1 + chance_score) * 100.0).round() / 100.0;


       println!("**{} - {}/5 rating:**\n{}\n", option_info[0], score, option_info[1]);
      
       if score > top_two[0].1 {
           top_two[1] = top_two[0];
           top_two[0] = (option_info[0].split(" (").collect::<Vec<&str>>()[0], score);
       } else if score > top_two[1].1 {
           top_two[1] = (option_info[0].split(" (").collect::<Vec<&str>>()[0], score);
       }
   }


   let first_place_score = top_two[0].1;
   let first_place_name = top_two[0].0;
   let second_place_score = top_two[1].1;
   let second_place_name = top_two[1].0;


   let threshold = ((first_place_score - (first_place_score * 0.02)) * 100.0).round() / 100.0;


   let percent_first_ranked_over = ((first_place_score + (fastrand::f64() * 14.0) + 42.0) * 100.0).round() / 100.0;
   let percent_second_total_ranked_over = (((fastrand::f64() * 6.0) + 94.0) * 100.0).round() / 100.0 - percent_first_ranked_over;
   let winner = if percent_first_ranked_over > percent_second_total_ranked_over {first_place_name} else {second_place_name};


   println!("Top two - {first_place_name}: {first_place_score}/5, {second_place_name}: {second_place_score}/5. For a co-presidency, the rule is \
   that the second placing candidate must be within 3% of the winning candidate (we do not allow three presidents).\n");


   if second_place_score > threshold {
       println!("{second_place_name}'s score is greater than the threshold of {threshold:.2}, so we will have co-presidents!");
   } else {
       println!("{second_place_name}'s score did not meet the threshold of {threshold:.2}. \
               Under STAR voting, the winner is determined by seeing what percentage of people rank {first_place_name} over {second_place_name} \
               and what percentage rank {second_place_name} over {first_place_name}. {percent_first_ranked_over:.2}% of people ranked {first_place_name} \
               over {second_place_name}, \
               while {percent_second_total_ranked_over:.2}% ranked {second_place_name} over {first_place_name}.");
       println!("This means {winner} is the President of the United Cold Nation!")
   }
}