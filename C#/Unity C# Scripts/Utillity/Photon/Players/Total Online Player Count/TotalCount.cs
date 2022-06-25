using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Photon.Pun;

public class TotalCount : MonoBehaviour
{
    //Refs
    public TMP_Text totalPlayersOnline;
    private LoadBalancingClient loadBalancingClient;

    void Update()
    {
        int totalPlayers = loadBalancingClient.PlayersOnMasterCount + loadBalancingClient.PlayersInRoomsCount;
        totalPlayersOnline.text = ("Total Players Online: " + totalPlayers);
    }
}