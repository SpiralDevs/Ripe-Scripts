using UnityEngine;

public class player_session_count : MonoBehaviour 
{
    void Awake()
    {
        SessionNumber = PlayerPrefs.GetString("unity.player_session_count");
        if (SessionNumber == "0")
        {
            return;
        }
        else
        {
            SceneManager.LoadScene("Main Menu");
        }
        Debug.Log("This player has played "+ SessionNumber + "times.");
    }
}